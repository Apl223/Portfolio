#!/bin/bash   <!-- Shebang line to indicate the script is written in bash -->
source ./scan.lib   <!-- Source scan.lib script -->

<!-- While loop with getopts to parse command line options -->
while getopts "m:i" OPTION;
  do case $OPTION in 
    m) 
      MODE=$OPTARG   <!-- Set MODE variable to the value of the option argument passed to -m -->
      ;;
    i)
      INTERACTIVE=true   <!-- Set INTERACTIVE variable to true if the -i option is passed -->
      ;;
    esac 
  done 

# Function to perform domain scanning
scan_domain(){
  DOMAIN=$1   # Set DOMAIN variable to the first argument passed to the function
  DIRECTORY=${DOMAIN}_recon   # Set DIRECTORY variable to the domain name followed by _recon
  echo "Creating directory $DIRECTORY."   # Print message to indicate the directory is being created
  mkdir $DIRECTORY   # Create the directory
  case $MODE in   # Perform a specific type of scan based on the value of MODE variable
    nmap-only)
      nmap_scan   # Call the nmap_scan function
      ;;
    dirsearch-only)
      dirsearch_scan   # Call the dirsearch_scan function
      ;;
    crt-only)
      crt_scan   # Call the crt_scan function
      ;;
    *)
      nmap_scan   # Call the nmap_scan function
      dirsearch_scan   # Call the dirsearch_scan function
      crt_scan   # Call the crt_scan function
      ;;
  esac
}

# Function to generate a report of the domain scan
report_domain(){
  DOMAIN=$1   # Set DOMAIN variable to the first argument passed to the function
  DIRECTORY=${DOMAIN}_recon   # Set DIRECTORY variable to the domain name followed by _recon
  echo "Generating recon report for $DOMAIN..."   # Print message to indicate the report is being generated
  TODAY=$(date)   # Set TODAY variable to the current date
  echo "This scan was created on $TODAY" > $DIRECTORY/report   # Add the current date to the report file
  if [ -f $DIRECTORY/nmap ];then   # If the nmap file exists, add the nmap results to the report
    echo "Results for Nmap:" >> $DIRECTORY/report
    grep -E "^\s*\S+\s+\S+\s+\S+\s*$" $DIRECTORY/nmap >> $DIRECTORY/report
  fi
  if [ -f $DIRECTORY/dirsearch ];then   # If the dirsearch file exists, add the dirsearch results to the report
    echo "Results for Dirsearch:" >> $DIRECTORY/report
    cat $DIRECTORY/dirsearch >> $DIRECTORY/report
  fi
  if [ -f $DIRECTORY/crt ];then   # If the crt file exists, add the crt results to the report
    echo "Results for crt.sh:" >> $DIRECTORY/report
    jq -r ".[] | .name_value" $DIRECTORY/crt >> $DIRECTORY/report
  fi
}

# If the INTERACTIVE variable is set to true, enter an interactive loop to ask for domain names
if [ $INTERACTIVE ];then
  INPUT="BLANK"
  while [ $INPUT != "quit" ];do
    echo "Please enter a domain!"   # Prompt user to enter a domain name
    read INPUT   # Read user input
    if [ $INPUT != "quit" ];then
      scan_domain $INPUT   # Call the scan_domain function with the user input as an argument
      report_domain $INPUT   # Call the report_domain function with the user
    fi
  done
else
  for i in "${@:$OPTIND:$#}";do
    scan_domain $i
    report_domain $i
  done
fi




#!/usr/bin/python3
import json, sys

def main():
  severity_filter = ['warning', 'danger']
  results_file = sys.argv[1]
  if len(sys.argv) == 3:
    severity_filter = [sys.argv[2]]
  results = {}
  with open(results_file) as f:
    json_payload = f.readlines()[1]
    results = json.loads(json_payload)

  for service_k,service_v in results['services'].items():
    print(service_k)
    for finding_k,finding_v in service_v['findings'].items():
      if finding_v['level'] in severity_filter:
        print(f"  {finding_k} : {finding_v['level']}")
        if len(finding_v['items']) == 0:
          print('    No findings')
        else:
          for item in finding_v['items']:
            print('    '+item)

if __name__ == '__main__':
  main()
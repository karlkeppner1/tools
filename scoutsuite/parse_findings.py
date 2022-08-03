#!/usr/bin/python3
import json, sys

def main():
  level_filter = ['warning', 'danger']
  findings_file = sys.argv[1]
  if len(sys.argv) == 3:
    level_filter = [sys.argv[2]]
  findings = {}
  results = {}
  with open(findings_file) as f:
    json_payload = f.readlines()[1]
    findings = json.loads(json_payload)

  for service_k,service_v in findings['services'].items():
    for finding_k,finding_v in service_v['findings'].items():
      if finding_v['level'] in level_filter:
        if len(finding_v['items']) > 0:
          if not service_k in results:
            results[service_k] = {}
          if not finding_k in results[service_k]:
            results[service_k][finding_k] = []
          for item in finding_v['items']:
            results[service_k][finding_k].append(item)
  for service_k,service_v in results.items():
    print(service_k)
    for finding_k,finding_v in service_v.items():
      if len(finding_v) > 0:
        print(f"  {finding_k} : {findings['services'][service_k]['findings'][finding_k]['level']}")
        for item in finding_v:
          print('    '+item)
        
if __name__ == '__main__':
  main()

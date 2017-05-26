#Zabbix discovery scripts (LLD)
##Discover block devices

Pass either `disk`, `part`, `rom` or any other `TYPE` as an argument to this
script and it'll use `lsblk --pairs` to filter based on `TYPE`

The output is in JSON format that Zabbix understands: 

```
./blk.py disk | jq .
{
  "data": [
    {
      "{#DEVICE}": "sda"
    },
    {
      "{#DEVICE}": "sdb"
    }
  ]
}
./blk.py part | jq .
{
  "data": [
    {
      "{#DEVICE}": "sda1"
    },
    {
      "{#DEVICE}": "sda2"
    },
    {
      "{#DEVICE}": "sda5"
    },
    {
      "{#DEVICE}": "sdb1"
    }
  ]
}
./blk.py rom | jq .
{
  "data": [
    {
      "{#DEVICE}": "sr0"
    }
  ]
}
```

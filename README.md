## What is this?

It takes a csv, from `input/` which should be called `chrome_extensions_installed.csv`, this must conform to the format of `serial number,"extensionid1, extensionid2, extensionid3, etc, etc"` in order for it to work as expected.

## Configuration

There is only 1 thing that needs configuration, `config/extensions_mapper.json`. This should contain an array that looks like the below of any know extensions, the only thing that has to match is the extension ID, the name and publisher then get pulled through to the results file _if_ it can find a matching ID in the CSV.
```javascript
[
    {
        "id":"exampleChromeExtensionID",
        "extension_name":"extension_name",
        "publisher":"nameOfPublisher"
    },
]
```


At this point, you should be able to run it and there will be 4 files created in `result/`:

`extensions_known.json` - This will contain any extensions that are found in the `config/extensions_mapper.json` file.
```javascript
[
    {
        "id": "ggjhpefgjjfobnfoldnjipclpcfbgbhl", 
        "extension_name": "My Apps Secure Sign-in Extension", 
        "publisher": "Microsoft", 
        "count": 1
    }
]
```
`extensions_unknown.json` - This will contain any extensions that are not found in the `config/extensions_mapper.json` file.
```javascript
[
    {
        "id": "exampleID", 
        "count": 1
    }
]
```
`extensions_list_with_duplicates.json` - This is the raw data that the script loads, it writes it to file before processing the data encase you want access to the raw data



## Issues/suggestions

Any issues please raise on the github repo, or feel free to message me on twitter or the macadmins slack.

If anyone has any suggestions for automating the collection of the IDs/name/publisher please reach out to me :)

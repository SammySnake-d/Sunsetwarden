import json

with open("clients/apps/browser/src/manifest.json", "r", encoding="utf-8") as f:
    orig = json.load(f)

orig["name"] = "Sunsetvault"
orig["short_name"] = "Sunsetvault"
orig["author"] = "Sunset Edu. & Tech. Group and Bitwarden® community"
orig["homepage_url"] = "https://github.com/SunsetMkt/Sunsetvault"
orig["browser_action"]["default_title"] = "Sunsetvault"
orig["sidebar_action"]["default_title"] = "Sunsetvault"
del orig["applications"]["gecko"]["id"]
orig["description"] = (
    "Sunsetvault is an exclusive build of the popular open source password manager, designed for internal use by SETG."
)
orig["icons"] = {
    "16": "images/icon16_sunset.png",
    "32": "images/icon32_sunset.png",
    "48": "images/icon48_sunset.png",
    "128": "images/icon128_sunset.png",
}

if len(orig["description"]) > 132:
    raise ValueError("Description too long")

with open("clients/apps/browser/src/manifest.json", "w", encoding="utf-8") as f:
    json.dump(orig, f, indent=2)
    print("Wrote manifest.json")

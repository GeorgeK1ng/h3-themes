import jstyleson as json
import sys

# Statická mapa příkazů → shortcuty
COMMAND_SHORTCUT_MAP = {
    "to new": "mainMenuNewGame",
    "to load": "mainMenuLoadGame",
    "highscores": "mainMenuHighScores",
    "to credits": "mainMenuCredits",
    "exit": "mainMenuQuit",
    "start single": "mainMenuSingleplayer",
    "to campaign": "mainMenuCampaign",
    "start multi": "mainMenuMultiplayer",
    "start tutorial": "mainMenuTutorial",
    "to main": "mainMenuBack",
    "load single": "mainMenuSingleplayer",
    "load multi": "mainMenuMultiplayer",
    "load campaign": "mainMenuCampaign",
    "load tutorial": "mainMenuTutorial",
    "campaigns sod": "mainMenuCampaignSod",
    "campaigns ab": "mainMenuCampaignAb",
    "campaigns roe": "mainMenuCampaignRoe",
    "campaigns wog": "mainMenuCampaignWog",
    "campaigns hota": "mainMenuCampaignHota",
    "campaigns chr": "mainMenuCampaignChr",
    "campaigns vcmi": "mainMenuCampaignVCMI",
    "start campaign": "mainMenuCampaignCustom"
}

def fix_shortcuts(data):
    items = data.get("window", {}).get("items", [])
    for section in items:
        for button in section.get("buttons", []):
            button.pop("hotkey", None)
            command = button.get("command")
            if command in COMMAND_SHORTCUT_MAP:
                button["shortcut"] = COMMAND_SHORTCUT_MAP[command]
    return data

def main(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    fixed = fix_shortcuts(data)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(fixed, f, indent=4, ensure_ascii=False)

    print(f"✅ Uloženo do: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Použití: python fix_shortcut.py <vstup.json> <vystup.json>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])

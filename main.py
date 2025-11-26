import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
    for nickname, info in players.items():
        race_data = info["race"]
        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={"description": race_data["description"]}
        )
        for skill in race_data["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                race=race,
                defaults={"bonus": skill["bonus"]}
            )
        guild_data = info.get("guild")
        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={"description": guild_data["description"]}
            )
        else:
            guild = None
        Player.objects.get_or_create(
            nickname=nickname,
            defaults={
                "email": info["email"],
                "bio": info["bio"],
                "race": race,
                "guild": guild
            }
        )


if __name__ == "__main__":
    main()

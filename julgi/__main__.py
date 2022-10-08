import argparse

from .battle import BattleManager
from .parse import parse_ko


def game(
    name1: str,
    name2: str,
    seed: str = "",
    skill_file_path: str = "julgi/skill/skill_ko.yml",
    return_as_list: bool = True,
):
    battle_manager = BattleManager(name1, name2, seed, skill_file_path)
    result = battle_manager.battle()
    result_parse = parse_ko(result)

    if return_as_list:
        return result_parse

    return "\n".join(result_parse)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("name1", type=str)
    parser.add_argument("name2", type=str)
    parser.add_argument("--seed", type=str)
    parser.add_argument(
        "-f", "--skill-file-path", type=str, default="julgi/skill/skill_ko.yml"
    )
    args = parser.parse_args()

    result = game(
        args.name1, args.name2, args.seed, args.skill_file_path, return_as_list=False
    )
    print(result)


if __name__ == "__main__":
    cli()

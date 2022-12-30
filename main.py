import os
import tomllib
import glob
from pprint import pprint
from typing import Any
from model.note import Note


def execute():
    settings = read_settings()
    notes = create_notes(settings["vaults"])

    # debug
    pprint(notes)


def read_settings() -> dict[str, Any]:
    """
    設定TOMLファイルを読み込んで返します。
    :return: 設定TOMLデータ
    """
    with open("./settings.toml", mode="rb") as f:
        settings = tomllib.load(f)
        return settings


def create_notes(vaults: dict[str, Any]) -> list[Note]:
    """
    Obsidianノート情報を作成します。
    :param vaults: 読み込むvaultのパスリスト
    :return: ノート情報のリスト
    """
    notes = []
    for vault in vaults:
        file_list = get_file_list(vault)

        for file in file_list:
            full_path = file
            vault_name = get_vault_name(vault)
            file_name = os.path.basename(file)
            obsidian_link = get_obsidian_link(file)
            with open(file, mode="r", encoding="UTF-8") as f:
                contents = f.readlines()
            # TODO 作成中
            note_id = 0
            create_date = ""
            category = ""
            tags = ""
            mocs = ""
            header1 = ""
            note = Note(full_path, vault_name, file_name, obsidian_link,
                        note_id, create_date, category, tags, mocs, header1)
            notes.append(note)

    return notes


def get_file_list(vault: str) -> list[str]:
    """
    Markdownファイルの一覧を取得します。
    :param vault: 読み込むvaultのパス
    :return: Markdownファイルのリスト
    """
    return glob.glob(vault + "/**/*.md", recursive=True)


def get_vault_name(vault: str) -> str:
    """
    vaultの名前を取得します。
    :param vault: vaultのフルパス
    :return: vault名
    """
    sp = os.path.split(vault)
    return sp[-1]


def get_obsidian_link(file_path: str) -> str:
    """
    Obsidian URIを取得します。
    :param file_path: ファイルパス
    :return: Obsidian URI
    Obsidian URIの仕様は「Obsidian URIの利用 - Obsidian 日本語ヘルプ」を参照してください。
    https://publish.obsidian.md/help-ja/%E9%AB%98%E5%BA%A6%E3%81%AA%E3%83%88%E3%83%94%E3%83%83%E3%82%AF/Obsidian+URI%E3%81%AE%E5%88%A9%E7%94%A8
    """
    # TODO 作成中
    return ""


if __name__ == '__main__':
    execute()

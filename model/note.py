import dataclasses
import datetime


@dataclasses.dataclass
class Note:
    """
    Obsidianノートの情報
    """
    full_path: str
    """ファイルのフルパス"""
    vault_name: str
    """vault名"""
    file_name: str
    """ファイル名"""
    obsidian_link: str
    """Obsidianへのリンク"""
    note_id: int
    """ID"""
    create_date: datetime
    """作成日"""
    category: str
    """カテゴリ"""
    tags: []
    """タグ"""
    mocs: []
    """MOC"""
    header1: str
    """ヘッダー1の文字列"""

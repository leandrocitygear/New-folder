import sqlite3

DB_NAME = "game_progress.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT UNIQUE,
            max_level INTEGER             
        )
    """)
    conn.commit()
    conn.close()

def save_progress(player_name, level):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT max_level 
        FROM player_progress
        WHERE player_name = ? 
    """, (player_name,))

    result = cursor.fetchone()

    if result is None:

        cursor.execute("""
            INSERT INTO player_progress (player_name, max_level)
            VALUES (?, ?)
        """, (player_name, level))

    else:
        current_max = result[0]

        if level > current_max:
            cursor.execute("""
                UPDATE player_progress
                SET max_level = ?
                WHERE player_name = ?
            """, (level, player_name))
    
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT player_name, max_level
        FROM player_progress
        ORDER BY max_level DESC
        LIMIT 10
    """)

    players = cursor.fetchall()

    conn.close()

    return players

def remove_invalid_levels():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM player_progress
        WHERE max_level > 4
    """)

    conn.commit()
    conn.close()

def clear_database():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM player_progress")

    conn.commit()
    conn.close()
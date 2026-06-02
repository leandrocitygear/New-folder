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
            player_name TEXT,
            max_level INTEGER             
        )
    """)
    conn.commit()
    conn.close()

def save_progress(player_name, level):
    conn = connect()
    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO player_progress (player_name, max_level)
        VALUES (?, ?)
    """, (player_name, level))

    
    conn.commit()
    conn.close()

def get_leaderboard():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT player_name, max_level
        FROM player_progress
        ORDER BY id DESC
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
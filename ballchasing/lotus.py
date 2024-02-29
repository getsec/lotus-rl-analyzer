from dataclasses import dataclass


@dataclass(frozen=True)
class GameData:
    """Ballchasing data for analyzing from a single player section of a replay"""

    # general
    name: str
    player_id: str
    replay_id: str

    # core
    shots: int
    goals: int
    saves: int
    score: int
    shooting_percentage: int

    # boost
    bpm: int
    bcpm: float
    avg_amount: float
    time_boost_zero: float

    # movement
    avg_speed: int
    total_distance: int
    time_supersonic_speed: float
    time_boost_speed: float
    time_slow_speed: float

    #demo
    demo_inflicted: int = 0
    demo_taken: int = 0

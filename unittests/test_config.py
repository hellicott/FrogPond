
class Config:
    # Frog parameters
    frog_min_jump_distance = 10  # FLOAT must be greater than 0
    frog_max_jump_distance = 20  # FLOAT must be greater than of equal to min jump
    number_of_frogs_in_game = 6  # INT must be greater than or equal to 2

    # Lilly pad parameters
    lilly_pad_radius_max_percentage_of_pond_size = 10  # FLOAT must be larger than 2 (the min %)
    number_of_lilly_pads_on_pond = 30  # INT must be greater than 1

    # Pond parameters
    pond_radius = 20  # FLOAT must be greater than 0

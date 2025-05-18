from build_map import build_game_map
import print_message as pm

def main():
    game_map = build_game_map()
    pm.print_welcome()
    pm.print_map(game_map)
    pm.print_artifacts_list(game_map)

if __name__ == "__main__":
    main()

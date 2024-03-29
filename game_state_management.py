from format_numbers import FormattedNumber
from offline import calculate_offline_earnings
import json
import time

class GameStateManager:
    def __init__(self, upgrades):
        self.upgrades = upgrades
        self.last_active_time = None


    def load_or_create_game_state(self, upgrades):
        try:
            # Attempt to load the game state from the save file
            self.load_game_state()
        except FileNotFoundError:
            # If the save file is not found, continue with the initial state
            pass

    def save_game_state(self, filename='save/baconfactory_savestate.json'):
        # Convert the selected attributes to a dictionary
        last_active_time = time.time()
        save_data = GameStateManager.to_dict(self, self.upgrades, last_active_time)
        # print(save_data)

        # Save the dictionary to a JSON file
        with open(filename, 'w') as file:
            json.dump(save_data, file)
            print('Game saved!')

    def autosave_every_30s(self, pygame, autosave_timer):
        current_time2 = pygame.time.get_ticks()
        elapsed_time2 = current_time2 - autosave_timer[0]
        if elapsed_time2 >= 30000:
            self.save_game_state()
            autosave_timer[0] = current_time2

    def load_game_state(self, filename='save/baconfactory_savestate.json'):
        try:
            with open(filename, 'r') as file:
                # Check if the file is empty
                if file.read(1):
                    file.seek(0)  # Reset file read position
                    load_data = json.load(file)
                    print('Existing save loaded!')
                    GameStateManager.from_dict(self, load_data, self.upgrades)
                    offline_earnings = calculate_offline_earnings(load_data['last_active_time'], self.upgrades.balance_per_second.value)
                    self.upgrades.balance.value += offline_earnings
                    self.upgrades.recalculate_upgrade_costs()
                else:
                    print("Save file is empty. Continuing with the initial state.")
        except FileNotFoundError:
            print("Save file not found. Continuing with the initial state.")

    def to_dict(self, upgrades, last_active_time):
        # Create a dictionary with only the attributes you want to save
        save_data = {
            'balance': upgrades.balance.value,
            'balance_per_second': upgrades.balance_per_second.value,
            'click_rate': upgrades.click_rate.value,
            'click_multiplier': upgrades.click_multiplier.value,
            'total_clicks': upgrades.total_clicks.value,
            'upgrade_1_cost': upgrades.upgrade_1_cost.value,
            'upgrade_1_owned': upgrades.upgrade_1_owned.value,
            'upgrade_1_multiplier': upgrades.upgrade_1_current_multiplier.value,
            'upgrade_1_current_bps': upgrades.upgrade_1_current_bps.value,
            'upgrade_2_owned': upgrades.upgrade_2_owned.value,
            'upgrade_2_cost': upgrades.upgrade_2_cost.value,
            'upgrade_2_current_bps': upgrades.upgrade_2_current_bps.value,
            'upgrade_2_multiplier': upgrades.upgrade_2_current_multiplier.value,
            'upgrade_3_cost': upgrades.upgrade_3_cost.value,
            'upgrade_3_owned': upgrades.upgrade_3_owned.value,
            'upgrade_3_multiplier': upgrades.upgrade_3_current_multiplier.value,
            'upgrade_3_current_bps': upgrades.upgrade_3_current_bps.value,
            'upgrade_4_cost': upgrades.upgrade_4_cost.value,
            'upgrade_4_owned': upgrades.upgrade_4_owned.value,
            'upgrade_4_multiplier': upgrades.upgrade_4_current_multiplier.value,
            'upgrade_4_current_bps': upgrades.upgrade_4_current_bps.value,
            'upgrade_5_cost': upgrades.upgrade_5_cost.value,
            'upgrade_5_owned': upgrades.upgrade_5_owned.value,
            'upgrade_5_multiplier': upgrades.upgrade_5_current_multiplier.value,
            'upgrade_5_current_bps': upgrades.upgrade_5_current_bps.value,
            'upgrade_6_cost': upgrades.upgrade_6_cost.value,
            'upgrade_6_owned': upgrades.upgrade_6_owned.value,
            'upgrade_6_multiplier': upgrades.upgrade_6_current_multiplier.value,
            'upgrade_6_current_bps': upgrades.upgrade_6_current_bps.value,
            'upgrade_7_cost': upgrades.upgrade_7_cost.value,
            'upgrade_7_owned': upgrades.upgrade_7_owned.value,
            'upgrade_7_multiplier': upgrades.upgrade_7_current_multiplier.value,
            'upgrade_7_current_bps': upgrades.upgrade_7_current_bps.value,
            'upgrade_8_cost': upgrades.upgrade_8_cost.value,
            'upgrade_8_owned': upgrades.upgrade_8_owned.value,
            'upgrade_8_multiplier': upgrades.upgrade_8_current_multiplier.value,
            'upgrade_8_current_bps': upgrades.upgrade_8_current_bps.value,
            'last_active_time': last_active_time,
        }
        return save_data

    def from_dict(self, data, upgrades):
        upgrades.balance = FormattedNumber(data['balance'])
        upgrades.balance_per_second = FormattedNumber(data['balance_per_second'])
        upgrades.click_rate = FormattedNumber(data['click_rate'])
        upgrades.click_multiplier = FormattedNumber(data['click_multiplier'])
        upgrades.total_clicks = FormattedNumber(data['total_clicks'])
        upgrades.upgrade_1_cost.value = data['upgrade_1_cost']
        upgrades.upgrade_1_owned.value = data['upgrade_1_owned']
        upgrades.upgrade_1_current_multiplier.value = data['upgrade_1_multiplier']
        upgrades.upgrade_1_current_bps.value = data['upgrade_1_current_bps']
        upgrades.upgrade_2_cost.value = data['upgrade_2_cost']
        upgrades.upgrade_2_owned.value = data['upgrade_2_owned']
        upgrades.upgrade_2_current_multiplier.value = data['upgrade_2_multiplier']
        upgrades.upgrade_2_current_bps.value = data['upgrade_2_current_bps']
        upgrades.upgrade_3_cost.value = data['upgrade_3_cost']
        upgrades.upgrade_3_owned.value = data['upgrade_3_owned']
        upgrades.upgrade_3_current_multiplier.value = data['upgrade_3_multiplier']
        upgrades.upgrade_3_current_bps.value = data['upgrade_3_current_bps']
        upgrades.upgrade_4_cost.value = data['upgrade_4_cost']
        upgrades.upgrade_4_owned.value = data['upgrade_4_owned']
        upgrades.upgrade_4_current_multiplier.value = data['upgrade_4_multiplier']
        upgrades.upgrade_4_current_bps.value = data['upgrade_4_current_bps']
        upgrades.upgrade_5_cost.value = data['upgrade_5_cost']
        upgrades.upgrade_5_owned.value = data['upgrade_5_owned']
        upgrades.upgrade_5_current_multiplier.value = data['upgrade_5_multiplier']
        upgrades.upgrade_5_current_bps.value = data['upgrade_5_current_bps']
        upgrades.upgrade_6_cost.value = data['upgrade_6_cost']
        upgrades.upgrade_6_owned.value = data['upgrade_6_owned']
        upgrades.upgrade_6_current_multiplier.value = data['upgrade_6_multiplier']
        upgrades.upgrade_7_current_bps.value = data['upgrade_6_current_bps']
        upgrades.upgrade_7_cost.value = data['upgrade_7_cost']
        upgrades.upgrade_7_owned.value = data['upgrade_7_owned']
        upgrades.upgrade_7_current_multiplier.value = data['upgrade_7_multiplier']
        upgrades.upgrade_7_current_bps.value = data['upgrade_7_current_bps']
        upgrades.upgrade_8_cost.value = data['upgrade_8_cost']
        upgrades.upgrade_8_owned.value = data['upgrade_8_owned']
        upgrades.upgrade_8_current_multiplier.value = data['upgrade_8_multiplier']
        upgrades.upgrade_8_current_bps.value = data['upgrade_8_current_bps']
        self.last_active_time = data['last_active_time']

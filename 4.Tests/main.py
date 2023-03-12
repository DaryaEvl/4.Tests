
def task_1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    filtered_list = []
    for visit in geo_logs:
        keys = visit.keys()
        values = visit.values()
        for city, country in values:
            if country == 'Россия':
                filtered_list.append(list(keys))
    return filtered_list

def task_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    unique_identifier = []
    values = list(ids.values())
    for list_identifier in values:
        for identifier in list_identifier:
            if identifier not in unique_identifier:
               unique_identifier.append(identifier)
    return unique_identifier



def task_4():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    max_volume = 0
    max_channel = 0
    for sales_channel in stats:
        volume_channel = int(stats[sales_channel])
        if volume_channel >= max_volume:
            max_volume = volume_channel
            max_channel = sales_channel
    return max_channel






def calc_of_the_cost_of_delivery(distance: int, size: str, fragility: bool, workload: str) -> int | str:
    cost = 0
    min_delivery_cost = 400

    if distance < 0:
        return 'Distance cannot be a negative value'
    elif distance <= 2:
        cost += 50
    elif 2 < distance <= 10:
        cost += 100
    elif 10 < distance <= 30:
        cost += 200
    elif 30 < distance:
        cost += 300

    if size == 'small':
        cost += 100
    elif size == 'big':
        cost += 200
    else:
        return 'Size must be small or big'

    if distance > 30 and fragility:
        return 'The distance may not be more than 30 km for a soft cargo'
    elif fragility:
        cost += 300

    if workload == 'very_high':
        cost *= 1.6
    elif workload == 'high':
        cost *= 1.4
    elif workload == 'medium':
        cost *= 1.2
    else:
        cost *= 1

    return max(min_delivery_cost, cost)


if name == 'main':
    distance_error = 'Distance cannot be a negative value'
    distance_error_for_soft_cargo = 'The distance may not be more than 30 km for a soft cargo'
    size_error = 'Size must be small or big'

    assert (calc_of_the_cost_of_delivery(1, 'small', True, 'very_high')) == 720
    assert (calc_of_the_cost_of_delivery(1, 'big', False, 'high')) == 400
    assert (calc_of_the_cost_of_delivery(2, 'small', False, 'medium')) == 400
    assert (calc_of_the_cost_of_delivery(2, 'big', True, 'other')) == 550

    assert (calc_of_the_cost_of_delivery(3, 'small', True, 'other')) == 500
    assert (calc_of_the_cost_of_delivery(5, 'big', False, 'very_high')) == 480
    assert (calc_of_the_cost_of_delivery(9, 'small', True, 'high')) == 700
    assert (calc_of_the_cost_of_delivery(10, 'big', False, 'medium')) == 400

    assert (calc_of_the_cost_of_delivery(11, 'small', True, 'medium')) == 720
    assert (calc_of_the_cost_of_delivery(20, 'big', False, 'other')) == 400
    assert (calc_of_the_cost_of_delivery(29, 'small', True, 'very_high')) == 960
    assert (calc_of_the_cost_of_delivery(30, 'big', False, 'high')) == 560

    assert (calc_of_the_cost_of_delivery(31, 'small', True, 'high')) == distance_error_for_soft_cargo
    assert (calc_of_the_cost_of_delivery(50, 'big', False, 'medium')) == 600
    assert (calc_of_the_cost_of_delivery(50, 'small', True, 'other')) == distance_error_for_soft_cargo
    assert (calc_of_the_cost_of_delivery(50, 'big', False, 'very_high')) == 800

    assert (calc_of_the_cost_of_delivery(-1, 'small', True, 'medium')) == distance_error
    assert (calc_of_the_cost_of_delivery(0, 'small', False, 'other')) == 400
    assert (calc_of_the_cost_of_delivery(0, 'medium', True, 'very_high')) == size_error

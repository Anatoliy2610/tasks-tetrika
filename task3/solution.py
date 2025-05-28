def get_lesson_time_slots(data, lesson_start, lesson_end):
    result = []
    for i in range(0, len(data), 2):
        coming_to_class = max(data[i], lesson_start)
        leaving_lesson = min(data[i + 1], lesson_end)
        if coming_to_class < leaving_lesson:
            result.append([coming_to_class, leaving_lesson])
    return result


def get_filter_data(lists):
    result = []
    for item in lists:
        if not result:
            result.append(item)
        else:
            if result[-1][1] >= item[0]:
                if result[-1][1] < item[1]:
                    result[-1] = [result[-1][0], item[1]]
            else:
                result.append(item)
    return result


def get_total_time(data_pupil, data_tutor):
    result = 0
    for interval_pupil in data_pupil:
        for interval_tutor in data_tutor:
            if interval_pupil[0] <= interval_tutor[0] < interval_pupil[1]:
                if interval_tutor[1] <= interval_pupil[1]:
                    result += (interval_tutor[1] - interval_tutor[0])
                else:
                    result += (interval_pupil[1] - interval_tutor[0])
            elif interval_tutor[0] < interval_pupil[1]:
                if interval_tutor[1] <= interval_pupil[1]:
                    result += (interval_tutor[1] - interval_pupil[0])
                else:
                    result += (interval_pupil[1] - interval_pupil[0])
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals.get('lesson')
    pupil_intervals = intervals.get('pupil')
    tutor_intervals = intervals.get('tutor')
    time_slots_pupil = get_lesson_time_slots(
        pupil_intervals,
        lesson_start,
        lesson_end
    )
    time_slots_tutor = get_lesson_time_slots(
        tutor_intervals,
        lesson_start,
        lesson_end
    )
    time_slots_pupil_filter = get_filter_data(time_slots_pupil)
    time_slots_tutor_filter = get_filter_data(time_slots_tutor)
    return get_total_time(time_slots_pupil_filter, time_slots_tutor_filter)

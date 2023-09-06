import math

def solution(fees, records):
    answer = []
    parking = []
    parking_time = []
    dict_cumulative_time = dict()
    for record in records:
        time, number, state = record.split(" ")
        if number not in parking:
            parking.append(number)
            parking_time.append(time)
        else:
            if number in dict_cumulative_time.keys():
                cumulative_time = dict_cumulative_time[number]
            else:
                cumulative_time = 0
            idx = parking.index(number)
            in_hour, in_minute = map(int, parking_time[idx].split(":"))
            out_hour, out_minute = map(int, time.split(":"))
            if in_minute > out_minute:
                out_hour -= 1
                out_minute += 60
            cumulative_time += out_minute - in_minute + (out_hour - in_hour) * 60
            dict_cumulative_time[number] = cumulative_time
            del parking[idx]
            del parking_time[idx]
    for idx in range(len(parking)):
        if parking[idx] in dict_cumulative_time.keys():
            cumulative_time = dict_cumulative_time[parking[idx]]
        else:
            cumulative_time = 0
        in_hour, in_minute = map(int, parking_time[idx].split(":"))
        out_hour, out_minute = 23, 59
        cumulative_time += out_minute - in_minute + (out_hour - in_hour) * 60
        dict_cumulative_time[parking[idx]] = cumulative_time
    for number, cumulative_time in dict_cumulative_time.items():
        if cumulative_time <= fees[0]:
            answer.append((number, fees[1]))
        else:
            answer.append((number, fees[1] + math.ceil((cumulative_time - fees[0]) / fees[2]) * fees[3]))
    answer.sort()
    fees = []
    for fee in answer:
        fees.append(fee[1])
    return fees
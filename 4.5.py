user_year = '1927'                                                             # str, 1927
mktrf_list = [0.97, 0.30, 0.00, 0.72]                                          # list, [0.97, 0.30, 0.00, 0.72]

avr_mktrf_list = float(sum(mktrf_list) / len(mktrf_list))                      # float, 0.4975
avr = round(avr_mktrf_list, 2)                                                 # float, 0.5

value = len(mktrf_list)                                                        # int, 4

max = max(mktrf_list)                                                          # int, 0.97
min = min(mktrf_list)                                                          # min, 0.0

print(
    f"{user_year} (Mkt-RF): {value} values, max {max}, min {min}, avg {avr}")  # str, 1927 (Mkt-RF): 4 values, max 0.97, min 0.0, avg 0.5

mktrf_1927 = [0.97, 0.30, 0.00, 0.72]                                          # list, [0.97, 0.30, 0.00, 0.72]

sorted_lst = sorted(mktrf_1927)                                                # list, [0.0, 0.3, 0.72, 0.97]
median_index = int(len(sorted_lst) / 2)                                        # int, 2

lvalue = sorted_lst[median_index - 1]                                          # 0.3, (index to left of middle)
rvalue = sorted_lst[median_index]                                              # 0.72, (index to right of middle)

median = (lvalue + rvalue) / 2                                                 # these two values summed and averaged

print(f"median is {median}\n"
      f"(average of {lvalue} and {rvalue})")

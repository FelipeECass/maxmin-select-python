def max_min_divide_conquer(p_arr, p_low, p_high):

    if p_low == p_high:
        return p_arr[p_low], p_arr[p_low]
    
    if p_high == p_low + 1:
        if p_arr[p_low] < p_arr[p_high]:
            return p_arr[p_low], p_arr[p_high]
        else:
            return p_arr[p_high], p_arr[p_low]

    v_mid = (p_low + p_high) // 2
    v_min1, v_max1 = max_min_divide_conquer(p_arr, p_low, v_mid)
    v_min2, v_max2 = max_min_divide_conquer(p_arr, v_mid + 1, p_high)

    v_overallMin = min(v_min1, v_min2)
    v_overallMax = max(v_max1, v_max2)

    return v_overallMin, v_overallMax


if __name__ == "__main__":
    v_lista = [42, 7, 19, 73, -5, 0, 88, 23, 17]
    v_min, v_max = max_min_divide_conquer(v_lista, 0, len(v_lista) - 1)

    print("Lista:", v_lista)
    print("Mínimo:", v_min)
    print("Máximo:", v_max)

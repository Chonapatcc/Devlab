import sys


def solve():
    # 1. อ่านข้อมูลทั้งหมดรวดเดียวเพื่อความเร็ว (Fast I/O)
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        Q = int(next(iterator))
    except StopIteration:
        return

    queries = []
    needed_points = set()
    
    # 0! = 1 เป็นค่าพื้นฐานที่ต้องมี
    needed_points.add(0)

    # 2. เก็บคำถามทั้งหมด และระบุจุดที่ต้องการ (Events)
    for _ in range(Q):
        n = int(next(iterator))
        m = int(next(iterator))
        queries.append((n, m))
        needed_points.add(n)
        needed_points.add(m)

    # เรียงลำดับจุดที่ต้องการจากน้อยไปมาก
    sorted_points = sorted(list(needed_points))
    
    # 3. คำนวณ Factorial แบบรอบเดียว (Sweep Line)
    # เก็บค่า factorial ของจุดที่ต้องการไว้ใน dict เพื่อประหยัด Memory
    fact_map = {}
    current_fact = 1
    current_n = 0
    
    MOD = 998244353

    # วนลูปแค่ถึงจุดสูงสุดที่ต้องการ ไม่จำเป็นต้องถึง 10^8 ถ้าโจทย์ไม่ถาม
    for point in sorted_points:
        if point == 0:
            fact_map[0] = 1
            continue
        
        # คูณค่าต่อจากจุดเดิม ไปจนถึงจุดใหม่
        # การใช้ range ใน PyPy เร็วมาก
        temp = current_fact
        for i in range(current_n + 1, point + 1):
            temp = (temp * i) % MOD
        
        current_fact = temp
        fact_map[point] = current_fact
        current_n = point

    # 4. แสดงผลคำตอบ
    results = []
    for n, m in queries:
        # สูตร: (n! / m!) % p  =>  (n! * inverse(m!)) % p
        # Fermat's Little Theorem: inverse(a) = a^(p-2) % p
        
        val_n = fact_map[n]
        val_m = fact_map[m]
        
        # คำนวณ Modular Inverse
        inv_m = pow(val_m, MOD - 2, MOD)
        
        ans = (val_n * inv_m) % MOD
        results.append(str(ans))

    print('\n'.join(results))

if __name__ == '__main__':
    solve()
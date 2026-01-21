#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

const int MOD = 998244353;

// ฟังก์ชันสำหรับหา Power (x^y % p) ใช้สำหรับหา Modular Inverse
long long power(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

// ฟังก์ชันหา Modular Inverse โดยใช้ Fermat's Little Theorem
long long modInverse(long long n) {
    return power(n, MOD - 2);
}

struct Query {
    int n, m, id;
};

int main() {
    // 1. Fast I/O: ปิด sync กับ stdio เพื่อให้อ่านเขียนไวที่สุด
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int Q;
    if (!(cin >> Q)) return 0;

    vector<Query> queries(Q);
    vector<int> checkpoints;
    
    // 0! = 1 เสมอ ใส่เป็นจุดตั้งต้น
    checkpoints.push_back(0); 

    // 2. รับ Input และเก็บจุดที่ต้องใช้ (n และ m)
    for (int i = 0; i < Q; i++) {
        cin >> queries[i].n >> queries[i].m;
        queries[i].id = i;
        checkpoints.push_back(queries[i].n);
        checkpoints.push_back(queries[i].m);
    }

    // 3. เรียงลำดับ Checkpoints และลบค่าซ้ำ
    sort(checkpoints.begin(), checkpoints.end());
    checkpoints.erase(unique(checkpoints.begin(), checkpoints.end()), checkpoints.end());

    // Map เพื่อเก็บค่า Factorial ของจุดที่ต้องการ (ใช้ Map ประหยัดเมมกว่า Array 10^8 ช่อง)
    // แต่ถ้า Q น้อยมาก (696) map ก็เร็วเพียงพอ ไม่ต้องใช้ Hash Table
    map<int, long long> fact_values;
    
    // กำหนดค่าเริ่มต้น
    long long current_fact = 1;
    int current_num = 0;
    fact_values[0] = 1;

    // 4. Sweep Line: วนลูปสร้าง Factorial รอบเดียว
    for (int point : checkpoints) {
        if (point == 0) continue;

        // คูณสะสมจากจุดเดิม ไปจนถึงจุดใหม่
        for (int i = current_num + 1; i <= point; i++) {
            current_fact = (current_fact * i) % MOD;
        }

        // บันทึกค่า
        fact_values[point] = current_fact;
        current_num = point;
    }

    // 5. คำนวณคำตอบแต่ละข้อ
    // n! / m! = n! * inv(m!)
    for (int i = 0; i < Q; i++) {
        long long fn = fact_values[queries[i].n];
        long long fm = fact_values[queries[i].m];
        
        long long inv_fm = modInverse(fm);
        long long ans = (fn * inv_fm) % MOD;

        cout << ans << "\n";
    }

    return 0;
}
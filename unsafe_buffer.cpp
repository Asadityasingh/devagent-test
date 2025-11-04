#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>

// ISSUE 1: Hardcoded credentials
const char* API_KEY = "sk_live_1234567890abcdef";
const char* DB_PASSWORD = "postgres_password_123";

// ISSUE 2: Global mutable state (race condition in multi-threaded context)
int global_counter = 0;

// ISSUE 3: Buffer overflow vulnerability
void process_input(char* user_input) {
    char buffer[16];
    // ISSUE: No bounds checking - buffer overflow
    strcpy(buffer, user_input);
    printf("Buffer: %s\n", buffer);
}

// ISSUE 4: SQL injection in C
void query_database(const char* user_id) {
    char query[256];
    // ISSUE: String concatenation - SQL injection
    sprintf(query, "SELECT * FROM users WHERE id=%s", user_id);
    printf("Query: %s\n", query);
}

// ISSUE 5: Memory leak - pointer not freed
void* allocate_memory(int size) {
    void* ptr = malloc(size);
    // ISSUE: Never freed - memory leak
    return ptr;
}

// ISSUE 6: Insecure random
int generate_token() {
    // ISSUE: Weak random number - predictable tokens
    return rand() % 10000;
}

// ISSUE 7: Integer overflow
int add_numbers(int a, int b) {
    // ISSUE: No overflow check
    return a + b;
}

// ISSUE 8: Complex nested logic
int validate_user(int age, int status, int role, int verified) {
    if (age > 18) {
        if (status == 1) {
            if (role == 2) {
                if (verified == 1) {
                    if (age < 100) {
                        return 1;
                    }
                }
            }
        }
    }
    return 0;
}

int main(int argc, char* argv[]) {
    // ISSUE 9: Command injection via system()
    if (argc > 1) {
        char cmd[512];
        // ISSUE: User input directly to system()
        sprintf(cmd, "echo %s", argv[1]);
        system(cmd);
    }
    
    // ISSUE 10: Use of dangerous functions
    char buffer[50];
    scanf("%s", buffer);  // Buffer overflow risk
    
    process_input(buffer);
    
    return 0;
}

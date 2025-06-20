#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int acc_no;
    char name[50];
    float balance;
} Account;

void createAccount() {
    Account acc;
    FILE *fp = fopen("accounts.dat", "ab");
    if (!fp) {
        printf("Error opening file!\n");
        return;
    }

    printf("Enter Account Number: ");
    scanf("%d", &acc.acc_no);
    printf("Enter Name: ");
    scanf(" %[^\n]", acc.name);
    printf("Enter Initial Deposit: ");
    scanf("%f", &acc.balance);

    fwrite(&acc, sizeof(Account), 1, fp);
    fclose(fp);
    printf("Account created successfully!\n");
}

void deposit() {
    int acc_no;
    float amount;
    Account acc;
    int found = 0;

    printf("Enter Account Number: ");
    scanf("%d", &acc_no);

    FILE *fp = fopen("accounts.dat", "rb+");
    if (!fp) {
        printf("File error.\n");
        return;
    }

    while (fread(&acc, sizeof(Account), 1, fp)) {
        if (acc.acc_no == acc_no) {
            printf("Enter deposit amount: ");
            scanf("%f", &amount);
            acc.balance += amount;
            fseek(fp, -sizeof(Account), SEEK_CUR);
            fwrite(&acc, sizeof(Account), 1, fp);
            printf("Deposit successful!\n");
            found = 1;
            break;
        }
    }

    if (!found)
        printf("Account not found.\n");

    fclose(fp);
}

void withdraw() {
    int acc_no;
    float amount;
    Account acc;
    int found = 0;

    printf("Enter Account Number: ");
    scanf("%d", &acc_no);

    FILE *fp = fopen("accounts.dat", "rb+");
    if (!fp) {
        printf("File error.\n");
        return;
    }

    while (fread(&acc, sizeof(Account), 1, fp)) {
        if (acc.acc_no == acc_no) {
            printf("Enter withdrawal amount: ");
            scanf("%f", &amount);
            if (acc.balance >= amount) {
                acc.balance -= amount;
                fseek(fp, -sizeof(Account), SEEK_CUR);
                fwrite(&acc, sizeof(Account), 1, fp);
                printf("Withdrawal successful!\n");
            } else {
                printf("Insufficient balance.\n");
            }
            found = 1;
            break;
        }
    }

    if (!found)
        printf("Account not found.\n");

    fclose(fp);
}

void checkBalance() {
    int acc_no;
    Account acc;
    int found = 0;

    printf("Enter Account Number: ");
    scanf("%d", &acc_no);

    FILE *fp = fopen("accounts.dat", "rb");
    if (!fp) {
        printf("File error.\n");
        return;
    }

    while (fread(&acc, sizeof(Account), 1, fp)) {
        if (acc.acc_no == acc_no) {
            printf("Name: %s\n", acc.name);
            printf("Balance: %.2f\n", acc.balance);
            found = 1;
            break;
        }
    }

    if (!found)
        printf("Account not found.\n");

    fclose(fp);
}

int main() {
    int choice;

    do {
        printf("\n--- Bank Management System ---\n");
        printf("1. Create Account\n");
        printf("2. Deposit\n");
        printf("3. Withdraw\n");
        printf("4. Check Balance\n");
        printf("5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: createAccount(); break;
            case 2: deposit(); break;
            case 3: withdraw(); break;
            case 4: checkBalance(); break;
            case 5: printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while (choice != 5);

    return 0;
}

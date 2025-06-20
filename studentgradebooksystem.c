#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100
#define SUBJECTS 3

typedef struct {
    char name[50];
    int roll;
    float marks[SUBJECTS];
    float percentage;
    char grade;
} Student;

void calculate(Student *s) {
    float total = 0;
    for (int i = 0; i < SUBJECTS; i++) {
        total += s->marks[i];
    }
    s->percentage = total / SUBJECTS;

    if (s->percentage >= 90) s->grade = 'A';
    else if (s->percentage >= 75) s->grade = 'B';
    else if (s->percentage >= 60) s->grade = 'C';
    else if (s->percentage >= 50) s->grade = 'D';
    else s->grade = 'F';
}

void writeToFile(Student s) {
    FILE *fp = fopen("students.dat", "ab");
    if (fp == NULL) {
        printf("Error opening file!\n");
        return;
    }
    fwrite(&s, sizeof(Student), 1, fp);
    fclose(fp);
}

void displayAll() {
    FILE *fp = fopen("students.dat", "rb");
    if (fp == NULL) {
        printf("No records found.\n");
        return;
    }

    Student s;
    printf("\n%-10s %-10s %-10s %-10s\n", "Roll", "Name", "Percent", "Grade");
    printf("--------------------------------------------------\n");
    while (fread(&s, sizeof(Student), 1, fp)) {
        printf("%-10d %-10s %-10.2f %-10c\n", s.roll, s.name, s.percentage, s.grade);
    }
    fclose(fp);
}

void findTopper() {
    FILE *fp = fopen("students.dat", "rb");
    if (fp == NULL) {
        printf("No records found.\n");
        return;
    }

    Student s, topper;
    float max = 0;
    int found = 0;
    while (fread(&s, sizeof(Student), 1, fp)) {
        if (!found || s.percentage > max) {
            max = s.percentage;
            topper = s;
            found = 1;
        }
    }
    fclose(fp);

    if (found) {
        printf("\nTopper:\n");
        printf("Name: %s\nRoll: %d\nPercentage: %.2f\nGrade: %c\n",
               topper.name, topper.roll, topper.percentage, topper.grade);
    }
}

void enterStudent() {
    Student s;
    printf("Enter name: ");
    scanf(" %[^\n]", s.name);
    printf("Enter roll number: ");
    scanf("%d", &s.roll);
    for (int i = 0; i < SUBJECTS; i++) {
        printf("Enter marks for subject %d: ", i + 1);
        scanf("%f", &s.marks[i]);
    }
    calculate(&s);
    writeToFile(s);
    printf("Student record saved.\n");
}

int main() {
    int choice;

    do {
        printf("\n--- Student Gradebook System ---\n");
        printf("1. Add Student\n");
        printf("2. Display All Students\n");
        printf("3. Show Topper\n");
        printf("4. Exit\n");
        printf("Choose an option: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: enterStudent(); break;
            case 2: displayAll(); break;
            case 3: findTopper(); break;
            case 4: printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while (choice != 4);

    return 0;
}

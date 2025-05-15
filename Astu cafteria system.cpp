/*
Ibrahim Kedir (UGR/37132/17, Section 37)
Meron Belayneh (UGR/37394/17, Section 37)
Tihetna Abiyu (UGR/37860/17, Section 37)
Muktar Suleyman (UGR/37472/17, Section 38)
Samuel Aschalew (UGR/37704/17, Section 37)
Yusuf abdulsemed ( Ugr/38268/17 ,section 38)
*/



#include <iostream>
#include <fstream>
#include <iomanip>
#include<sstream>
using namespace std;

struct Student {
    string id, name, department;
    bool isCafeStudent;
};

struct MealRecord {
    string studentId, mealType;
    double price;
};
const string CAFE_FILE = "cafe_students.dat";
const string NON_CAFE_FILE = "non_cafe_students.dat";
const string MEAL_FILE = "meal_records.dat";
const string PAYMENT_FILE = "pending_payments.dat";

// Helper function to mimic tolower() safely
char toLowerChar(char c) {
    if (c >= 'A' && c <= 'Z') return c + 32;
    return c;
}

// Utility functions
void saveToFile(const string& filename, const string& data) {
    fstream file(filename,ios::app);
    if (file){ file << data << "\n";

    }
    else {cerr << "Error saving to " << filename << endl;}
}

void clearFile(const string& filename) {
    ofstream file(filename);
    if (!file) cerr << "Error clearing " << filename << endl;
    else cout << filename << " cleared successfully.\n";
}

Student findStudent(const string& id) {
    const char* files[] = {CAFE_FILE.c_str(), NON_CAFE_FILE.c_str()};
    for (int i = 0; i < 2; i++) {
        ifstream file(files[i]);
        string line;
        while (getline(file, line)) {
            size_t pos1 = line.find(',');
            if (line.substr(0, pos1) == id) {
                Student s;
                s.id = id;
                size_t pos2 = line.find(',', pos1 + 1);
                s.name = line.substr(pos1 + 1, pos2 - pos1 - 1);
                size_t pos3 = line.find(',', pos2 + 1);
                s.department = line.substr(pos2 + 1, pos3 - pos2 - 1);
                s.isCafeStudent = (i == 0);  // First file is cafe students
                return s;
            }
        }
    }
    return {};
}

bool isValidNumber(const string& str) {
    for (char c : str) {
        if ((c < '0' || c > '9') && c != '.') {
            return false;
        }
    }
    return true;
}

bool hasMealToday(const string& id, const string& mealType) {
    ifstream file(MEAL_FILE);
    string line;
    while (getline(file, line)) {
        size_t p1 = line.find(',');
        size_t p2 = line.find(',', p1 + 1);
        if (line.substr(0, p1) == id && line.substr(p1 + 1, p2 - p1 - 1) == mealType)
            return true;
    }
    return false;
}

void displayMenu(const string& title, const pair<string, double> items[], int size) {
    cout << "\n===== " << title << " Menu =====\n";
    cout << left << setw(30) << "Item" << setw(10) << "Price\n";
    cout << string(40, '-') << '\n';
    for (int i = 0; i < size; i++)
        cout << setw(30) << items[i].first << setw(10) << fixed << setprecision(2) << items[i].second << " ETB\n";
    cout << string(40, '=') << '\n';
}

void transferMealsToPending() {
    ifstream mealFile(MEAL_FILE);
    ofstream paymentFile(PAYMENT_FILE, ios::app);

    if (!mealFile || !paymentFile) {
        cerr << "Error transferring meal records\n";
        return;
    }

    string line;
    while (getline(mealFile, line)) {
        paymentFile << line << "\n";
    }

    clearFile(MEAL_FILE);
    cout << "Meal records transferred to pending payments.\n";
}

//Student Menu Functions
void addStudentProfile() {
    char cont;
    do {
        Student s;
        cout << "\nEnter student ID (or '0' to return): ";
        cin >> s.id;

        if (s.id == "0") return;

        if (findStudent(s.id).id != "") {
            cout << "Student already exists!\n";
            continue;
        }

        cout << "Enter name: ";
        cin.ignore();
        getline(cin, s.name);

        cout << "Enter department: ";
        getline(cin, s.department);

        cout << "Is this a cafe student? (y/n): ";
        char choice;
        cin >> choice;
        s.isCafeStudent = (toLowerChar(choice) == 'y');

        saveToFile(s.isCafeStudent ? CAFE_FILE : NON_CAFE_FILE,s.id + "," + s.name + "," + s.department + "," + (s.isCafeStudent ? "1" : "0"));
        cout << "Student added successfully!\n";

        cout << "Add another student? (y/n): ";
        cin >> cont;
    } while (toLowerChar(cont) == 'y');
}

void searchStudent() {
    char cont;
    do {
        cout << "\nEnter student ID (or '0' to return): ";
        string id;
        cin >> id;

        if (id == "0") return;

        Student s = findStudent(id);
        if (s.id == "") {
            cout << "Student not found!\n";
            continue;
        }

        cout << "\nStudent Information:\n";
        cout << "ID: " << s.id << "\n";
        cout << "Name: " << s.name << "\n";
        cout << "Department: " << s.department << "\n";
        cout << "Type: " << (s.isCafeStudent ? "Cafe Student" : "Non-Cafe Student") << "\n";

        cout << "Search another student? (y/n): ";
        cin >> cont;
    } while (toLowerChar(cont) == 'y');
}

void printTotalPayment() {
    char cont;
    do {
        cout << "\nEnter student ID (or '0' to return): ";
        string id;
        cin >> id;

        if (id == "0") return;

        Student s = findStudent(id);
        if (s.id.empty()) {
            cout << "Student not found!\n";
            continue;
        }

        ifstream mealFile(MEAL_FILE);
        ifstream paymentFile(PAYMENT_FILE);
        string line;
        double total = 0.0;
        int count = 0;

        // Check current meal records
        if (mealFile.is_open()) {
            while (getline(mealFile, line)) {
                size_t p1 = line.find(',');
                size_t p2 = line.find(',', p1 + 1);
                if (line.substr(0, p1) == id) {
                    string priceStr = line.substr(p2 + 1);
                    if (isValidNumber(priceStr)) {
                        double nprice=0.0;
                        stringstream ss(priceStr);
                        ss>>nprice;
                        total+=nprice;
                    }
                }
            }
            mealFile.close();
        }

        // Check pending payment records
        if (paymentFile.is_open()) {
            while (getline(paymentFile, line)) {
                size_t p1 = line.find(',');
                size_t p2 = line.find(',', p1 + 1);
                if (line.substr(0, p1) == id) {
                    string priceStr = line.substr(p2 + 1);
                    if (isValidNumber(priceStr)) {
                        double nprice=0.0;
                        stringstream ss(priceStr);
                        ss>>nprice;
                        total+=nprice;                    }
                }
            }
            paymentFile.close();
        }

        cout << "\n=== Payment Summary for " << s.name << " ===\n";
        cout << "Total meals recorded: " << count << "\n";
        cout << "Total amount due: " << fixed << setprecision(2) << total << " ETB\n";

        cout << "\nCheck another student's payment? (y/n): ";
        cin >> cont;
    } while (toLowerChar(cont) == 'y');
}

// Cafeteria Menu
void cafeteriaMenu() {
    const pair<string, double> breakfastMenu[] = {
        {"Injera Firfir", 40.00}, {"Rice with bread", 45.00}, {"Macaroni", 20.00}, {"Salad", 15.00}
    };
    const pair<string, double> lunchMenu[] = {
        {"Tibs with Injera", 50.00}, {"Shiro with Injera", 35.00}, {"Pasta", 30.00}, {"Rice with Vegetables", 25.00}
    };
    const pair<string, double> dinnerMenu[] = {
        {"Lentil stew", 33.00}, {"Meat stew", 20.00}, {"Rice with meat", 15.00}, {"Rice with Vegetables", 10.00}
    };

    const char* types[] = {"Breakfast", "Lunch", "Dinner"};

    int choice;
    do {
        cout << "\n===== Cafeteria Menu =====\n";
        cout << "1. Breakfast\n2. Lunch\n3. Dinner\n4. Back\n";
        cout << "Select: ";
        cin >> choice;

        if (choice == 1) displayMenu(types[0], breakfastMenu, 4);
        else if (choice == 2) displayMenu(types[1], lunchMenu, 4);
        else if (choice == 3) displayMenu(types[2], dinnerMenu, 4);
        else if (choice != 4) cout << "Invalid choice!\n";
    } while (choice != 4);
}

// Ticker System
void tickerMenu() {
    const char* types[] = {"Breakfast", "Lunch", "Dinner"};
    const double prices[] = {33.00, 34.00, 33.00};

    char cont = 'y';
    while (toLowerChar(cont) == 'y') {
        cout << "\n===== Ticker System =====\n";
        cout << "\nEnter student ID (or '0' to return): ";
        string id;
        cin >> id;

        if (id == "0") return;

        Student s = findStudent(id);
        if (s.id == "") {
            cout << "Student not found!\n";
            continue;
        }

        // Reject non-cafe students
        if (!s.isCafeStudent) {
            cout << "Access denied: Only cafe students are allowed to use the ticker system.\n";
            continue;
        }

        cout << "\nMeal Types:\n";
        for (int i = 0; i < 3; i++)
            cout << i+1 << ". " << types[i] << "\n";

        cout << "Select meal type (1-3 or 0 to cancel): ";
        int choice;
        cin >> choice;

        if (choice == 0) continue;
        if (choice < 1 || choice > 3) {
            cout << "Invalid choice!\n";
            continue;
        }

        string mealType = types[choice-1];
        if (hasMealToday(id, mealType)) {
            cout << "Student already had " << mealType << " today!\n";
            continue;
        }

        stringstream ss;
        ss << prices[choice - 1];
        saveToFile(MEAL_FILE, id + "," + mealType + "," + ss.str());
        cout << mealType << " recorded for " << s.name << "\n";

        cout << "\nRecord another meal? (y/n): ";
        cin >> cont;
    }
}
// Menu Controllers
void studentMenuController() {
    int choice;
    do {
        cout << "\n===== Student Menu =====\n";
        cout << "1. Add student profile\n";
        cout << "2. Search student\n";
        cout << "3. Display student information\n";
        cout << "4. Print total payment\n";
        cout << "5. Back to main menu\n";
        cout << "6. Exist\n" << endl;
        cout << "Select: ";
        cin >> choice;

        switch(choice) {
            case 1: addStudentProfile(); break;
            case 2: searchStudent(); break;
            case 3: searchStudent(); break;
            case 4: printTotalPayment(); break;
            case 5: break;
            default: cout << "Invalid choice!\n";
        }
    } while (choice != 5);
}

void dailyCheckerMenu() {
    int choice;
    do {
        cout << "\n===== Daily Checker Menu =====";
        cout << "\n1. Student Services";
        cout << "\n2. Cafeteria Menu";
        cout << "\n3. Ticker System";
        cout << "\n4. Back to Main Menu";
        cout << "\nSelect: ";
        cin >> choice;

        switch(choice) {
            case 1: studentMenuController(); break;
            case 2: cafeteriaMenu(); break;
            case 3: tickerMenu(); break;
            case 4: return;
            default: cout << "Invalid choice!\n";
        }
    } while (choice != 4);
}

int main() {
    cout << "=== ASTU Cafeteria Management System ===\n";

    int choice;
    do {
        cout << "\nMain Menu:\n";
        cout << "1. Daily Checker Menu\n";
        cout << "2. Exit\n";
        cout << "Select: ";
        cin >> choice;

        switch(choice) {
            case 1: dailyCheckerMenu(); break;
            case 2:
                transferMealsToPending();
                cout << "Exiting system...\n";
                break;
            default: cout << "Invalid choice!\n";
        }
    } while (choice != 2);

    return 0;
}
    
    
    
    
/*
Ibrahim Kedir (UGR/37132/17, Section 37)
Meron Belayneh (UGR/37394/17, Section 37)
Tihetna Abiyu (UGR/37860/17, Section 37)
Muktar Suleyman (UGR/37472/17, Section 38)
Samuel Aschalew (UGR/37704/17, Section 37)
Yusuf abdulsemed ( Ugr/38268/17 ,section 38)
*/
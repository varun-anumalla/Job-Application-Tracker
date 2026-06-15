from tracker import ApplicationTracker

tracker = ApplicationTracker()

while True:

    print("\n")
    print("=" * 40)
    print("JOB APPLICATION TRACKER")
    print("=" * 40)

    print("1. Add Application")
    print("2. View Applications")
    print("3. Search Application")
    print("4. Update Status")
    print("5. Delete Application")
    print("6. Total Applications")
    print("7. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        tracker.add_application()

    elif choice == "2":
        tracker.view_applications()

    elif choice == "3":
        tracker.search_application()

    elif choice == "4":
        tracker.update_status()

    elif choice == "5":
        tracker.delete_application()

    elif choice == "6":
        tracker.total_applications()

    elif choice == "7":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid Choice")
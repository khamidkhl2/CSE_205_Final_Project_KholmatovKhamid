"""
Test and Demo File for Lost and Found Management System
This file demonstrates various features of the system.
"""

from lost_and_found import Item, LostAndFoundSystem, LostAndFoundApp


def test_item_class():
    """Test the Item class."""
    print("="*60)
    print("TEST 1: Item Class")
    print("="*60)
    
    # Create an item
    item = Item("ITEM001", "Laptop", "Electronics", "Library")
    print(f"Created Item: {item}")
    print(f"Item Dictionary: {item.to_dict()}")
    
    # Create item from dictionary
    item_dict = {
        "item_id": "ITEM002",
        "item_name": "Wallet",
        "category": "Accessories",
        "location_found": "Cafeteria",
        "status": "Claimed",
        "date_added": "2026-05-08 10:00:00"
    }
    item2 = Item.from_dict(item_dict)
    print(f"\nItem from Dictionary: {item2}")
    print()


def test_system_operations():
    """Test System Operations."""
    print("="*60)
    print("TEST 2: System Operations")
    print("="*60)
    
    # Create system instance
    system = LostAndFoundSystem("test_items.json")
    
    # Test 1: Generate IDs
    print(f"\nGenerated IDs:")
    print(f"  ID 1: {system.generate_item_id()}")
    
    # Test 2: Add items
    print(f"\nAdding items...")
    item1 = Item("TEST001", "Test Backpack", "Accessories", "Campus")
    item2 = Item("TEST002", "Test Phone", "Electronics", "Dorm")
    item3 = Item("TEST003", "Test Book", "Documents", "Library")
    
    system.items.extend([item1, item2, item3])
    system.save_items()
    print(f"  Added 3 items")
    
    # Test 3: Search
    print(f"\nSearch by category 'Electronics':")
    results = [item for item in system.items if "electronics" in item.category.lower()]
    for result in results:
        print(f"  - {result}")
    
    # Test 4: Status update
    print(f"\nUpdating item status...")
    if system.items:
        system.items[0].status = "Claimed"
        print(f"  Updated: {system.items[0]}")
    
    # Test 5: Statistics
    print(f"\nSystem Statistics:")
    claimed = sum(1 for item in system.items if item.status == "Claimed")
    unclaimed = sum(1 for item in system.items if item.status == "Unclaimed")
    print(f"  Total Items: {len(system.items)}")
    print(f"  Claimed: {claimed}")
    print(f"  Unclaimed: {unclaimed}")
    
    # Test 6: Category organization
    print(f"\nItems by Category:")
    categories = {}
    for item in system.items:
        if item.category not in categories:
            categories[item.category] = []
        categories[item.category].append(item)
    
    for category, items in sorted(categories.items()):
        print(f"  {category}: {len(items)} items")
    
    print()


def demonstrate_menu_features():
    """Demonstrate menu features."""
    print("="*60)
    print("TEST 3: Demonstrating System Features")
    print("="*60)
    print(f"""
The Lost and Found Management System includes:

CORE FEATURES:
1. ✓ Add Lost Item
   - Auto-generates unique item IDs (ITEM001, ITEM002, etc.)
   - Validates user input (non-empty, minimum length)
   - Automatic timestamp recording

2. ✓ View All Items
   - Displays all items in formatted table
   - Shows total count
   - Displays claimed/unclaimed statistics

3. ✓ Search Item
   - Search by name (case-insensitive, partial matching)
   - Search by category
   - Search by location found
   - Returns count of matching items

4. ✓ Mark Item as Claimed
   - Updates item status to "Claimed"
   - Validates item exists before updating
   - Shows confirmation message

5. ✓ Delete Item
   - Removes item from system using item ID
   - Confirms deletion
   - Automatically saves changes

BONUS FEATURES:
6. ✓ Sort Items by Category
   - Groups items by category
   - Shows item count per category
   - Displays all items under each category

7. ✓ View Statistics
   - Total items count
   - Claimed items (count and percentage)
   - Unclaimed items (count and percentage)
   - Items breakdown by category

DATA STORAGE:
✓ JSON File Storage
  - Automatic loading on startup
  - Automatic saving after updates
  - Error handling for missing/corrupted files
  - Handles missing file gracefully

INPUT VALIDATION:
✓ User Input Validation
  - Non-empty field validation
  - Minimum length validation
  - Case-insensitive operations
  - User-friendly error messages
""")
    print()


def show_sample_workflow():
    """Show a sample workflow."""
    print("="*60)
    print("SAMPLE WORKFLOW")
    print("="*60)
    print("""
Typical User Workflow:

1. START APPLICATION
   ↓
2. ADD ITEM
   User enters: Laptop, Electronics, Student Center
   System generates: ITEM006
   Status set to: Unclaimed
   Data saved to: items.json
   ↓
3. VIEW ALL ITEMS
   Display all items with statistics
   Output: 6 total items (4 unclaimed, 2 claimed)
   ↓
4. SEARCH FOR ITEM
   User searches for "Electronics"
   Display matching items
   ↓
5. MARK AS CLAIMED
   User marks ITEM006 as claimed
   Status updated to "Claimed"
   ↓
6. VIEW STATISTICS
   Display updated statistics
   Output: 6 total items (3 unclaimed, 3 claimed)
   ↓
7. EXIT
   All changes saved automatically
   Program terminates

Data Persistence:
- All changes persisted in items.json
- Can restart program and continue working
- No data loss between sessions
""")
    print()


def show_json_example():
    """Show JSON file example."""
    print("="*60)
    print("JSON FILE STRUCTURE")
    print("="*60)
    print("""
items.json Example:

[
    {
        "item_id": "ITEM001",
        "item_name": "Blue Backpack",
        "category": "Accessories",
        "location_found": "Library Building",
        "status": "Unclaimed",
        "date_added": "2026-05-08 10:30:00"
    },
    {
        "item_id": "ITEM002",
        "item_name": "iPhone 14",
        "category": "Electronics",
        "location_found": "Cafeteria",
        "status": "Claimed",
        "date_added": "2026-05-07 14:45:00"
    },
    {
        "item_id": "ITEM003",
        "item_name": "Student ID Card",
        "category": "Documents",
        "location_found": "Main Gate",
        "status": "Unclaimed",
        "date_added": "2026-05-08 09:15:00"
    }
]

Features:
✓ Valid JSON format
✓ Automatically created if missing
✓ Auto-updated after every change
✓ Can be edited manually (with valid JSON)
✓ Handles encoding properly
""")
    print()


if __name__ == "__main__":
    print("\n" + "*"*60)
    print("LOST AND FOUND MANAGEMENT SYSTEM - TEST & DEMO")
    print("*"*60 + "\n")
    
    # Run tests
    test_item_class()
    test_system_operations()
    demonstrate_menu_features()
    show_sample_workflow()
    show_json_example()
    
    print("="*60)
    print("TESTS COMPLETED")
    print("="*60)
    print("""
To run the interactive application:
  python lost_and_found.py

To view the existing sample data:
  1. Run: python lost_and_found.py
  2. Select: 2 (View All Items)

For more information, see README.md
""")

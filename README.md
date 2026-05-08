# Lost and Found Management System

A complete Python-based Lost and Found Management System with OOP design, JSON file storage, and a user-friendly menu interface.

## Features

### Core Features
1. **Add Lost Item** - Add new lost/found items with automatic unique ID generation
2. **View All Items** - Display all items in the system with statistics
3. **Search Item** - Search items by name, category, or location found
4. **Mark Item as Claimed** - Update item status to claimed
5. **Delete Item** - Remove items from the system

### Bonus Features
6. **Sort Items by Category** - View items organized by category
7. **View Statistics** - See total, claimed, and unclaimed item counts

## Project Structure

```
project/
├── lost_and_found.py      # Main application file
├── items.json             # JSON file for storing item data (auto-created)
└── README.md              # This file
```

## Architecture

### Classes

#### `Item`
Represents a lost or found item with the following attributes:
- `item_id`: Unique identifier (auto-generated: ITEM001, ITEM002, etc.)
- `item_name`: Name of the item
- `category`: Category of the item (e.g., Electronics, Clothing, Accessories)
- `location_found`: Location where item was found
- `status`: Status of item (Unclaimed/Claimed)
- `date_added`: Timestamp when item was added

Methods:
- `to_dict()`: Convert item to dictionary for JSON storage
- `from_dict()`: Create item from dictionary (deserialization)
- `__str__()`: String representation for display

#### `LostAndFoundSystem`
Manages all operations and data persistence:
- `load_items()`: Load items from JSON file with error handling
- `save_items()`: Automatically save items after updates
- `generate_item_id()`: Generate unique item IDs
- `validate_input()`: Validate user input
- `add_item()`: Add new item to system
- `view_all_items()`: Display all items with statistics
- `search_item()`: Search by name, category, or location
- `mark_as_claimed()`: Update item status
- `delete_item()`: Remove item from system
- `sort_by_category()`: Display items grouped by category
- `count_statistics()`: Show item statistics

#### `LostAndFoundApp`
Main application controller:
- `display_menu()`: Show main menu options
- `run()`: Run the application main loop

## Usage Instructions

### Running the Application

1. **Open Terminal/Command Prompt** and navigate to the project directory:
   ```bash
   cd c:\Users\Student\Desktop\project
   ```

2. **Run the application**:
   ```bash
   python lost_and_found.py
   ```

3. **Follow the menu** to perform desired operations

### Menu Options

```
1. Add Lost Item
   - Generates automatic item ID
   - Validates user input
   - Saves to JSON file

2. View All Items
   - Displays all items in table format
   - Shows item statistics (claimed/unclaimed counts)

3. Search Item
   - Search by name: Find items by partial name match
   - Search by category: Find items by category
   - Search by location: Find items by location found

4. Mark Item as Claimed
   - Update item status from "Unclaimed" to "Claimed"
   - Enter item ID to mark as claimed

5. Delete Item
   - Permanently remove an item from the system
   - Enter item ID to delete

6. Sort Items by Category (BONUS)
   - View all items organized by category
   - Shows count of items per category

7. View Statistics (BONUS)
   - Total items in system
   - Claimed items (count and percentage)
   - Unclaimed items (count and percentage)
   - Items breakdown by category

8. Exit
   - Save all data and exit the application
```

## Data Storage

### JSON File Format

Items are stored in `items.json` in the following format:

```json
[
    {
        "item_id": "ITEM001",
        "item_name": "Blue Backpack",
        "category": "Accessories",
        "location_found": "Library Building",
        "status": "Unclaimed",
        "date_added": "2026-05-08 10:30:00"
    }
]
```

### Data Persistence
- Items are automatically loaded when the program starts
- Changes are saved to JSON file immediately after every update
- Missing file errors are handled gracefully (fresh inventory)
- Corrupted JSON files are detected and handled safely

## Features in Detail

### Input Validation
- Ensures all fields are non-empty
- Minimum character validation
- Provides user-friendly error messages
- Prevents invalid operations on missing items

### Unique ID Generation
- Automatically generates unique IDs (ITEM001, ITEM002, etc.)
- IDs are sequential and never duplicated
- New items cannot have duplicate IDs

### Search Functionality
- Case-insensitive search
- Partial matching supported
- Multiple search criteria available
- Returns count of matching items

### Category Organization
- Default categories: Electronics, Clothing, Accessories, Jewelry, Documents, Other
- Custom categories can be added
- Category filtering available

## Sample Data

The system includes sample data in `items.json` with 5 items:
- 1 Blue Backpack (Unclaimed)
- 1 iPhone 14 (Claimed)
- 1 Gold Wedding Ring (Unclaimed)
- 1 Red Hoodie (Unclaimed)
- 1 Student ID Card (Claimed)

You can view this data by running the program and selecting option 2.

## Error Handling

The system handles various error scenarios:
- Missing JSON file: Creates new inventory
- Corrupted JSON file: Detects and handles gracefully
- File writing errors: Displays error message and continues
- Invalid user input: Prompts for re-entry
- Item not found: Notifies user with clear message

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Example Usage Workflow

```
1. Start application
2. Add a new lost item (automatically gets ID ITEM006)
3. Add another item (gets ID ITEM007)
4. View all items to see the newly added items
5. Search for an item by name
6. Mark an item as claimed
7. View statistics to see updated counts
8. Exit (all data is automatically saved)
```

## Tips

- Item IDs are case-insensitive (ITEM001 = item001)
- Search is case-insensitive for better user experience
- All changes are saved automatically to JSON file
- You can edit items.json directly, but ensure valid JSON format
- Use descriptive item names for easier searching
- Organize items by logical categories for better management

## Future Enhancements (Optional)

- Email notifications for claimed items
- User login/authentication
- Item images/attachments
- Advanced filtering options
- Export reports to PDF/CSV
- Date range filtering
- Multiple claim transactions per item
- Item condition details

## License

This project is created for educational purposes.

## Author

Created as a comprehensive Python learning project demonstrating:
- Object-Oriented Programming (OOP)
- JSON file handling
- Data persistence
- Input validation
- Menu-driven user interface
- Error handling
- File I/O operations

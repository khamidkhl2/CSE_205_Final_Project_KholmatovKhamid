# QUICK START GUIDE - Lost and Found Management System

## 1. INITIAL SETUP

### Prerequisites
- Python 3.6 or higher installed on your computer
- Access to a terminal/command prompt

### Check Python Installation
```bash
python --version
```

If Python is not installed, download it from https://www.python.org/

---

## 2. RUN THE APPLICATION

### Step 1: Open Terminal
- Windows: Press `Win + R`, type `cmd`, press Enter
- Navigate to the project folder:
  ```bash
  cd c:\Users\Student\Desktop\project
  ```

### Step 2: Run the Application
```bash
python lost_and_found.py
```

### Expected Output
```
************************************************************
Welcome to Lost and Found Management System
************************************************************

✓ Loaded 5 items from items.json

============================================================
LOST AND FOUND MANAGEMENT SYSTEM
============================================================

1. Add Lost Item
2. View All Items
3. Search Item
4. Mark Item as Claimed
5. Delete Item
6. Sort Items by Category (BONUS)
7. View Statistics (BONUS)
8. Exit
------------------------------------------------------------
Enter your choice (1-8):
```

---

## 3. TRY THESE OPERATIONS

### Option 1: View Sample Data
```
1. Press: 2
2. See all 5 sample items with statistics
3. Press Enter to return to menu
```

### Option 2: Search for an Item
```
1. Press: 3
2. Choose: 2 (Search by Category)
3. Enter: Electronics
4. See all electronics items
5. Press Enter to return to menu
```

### Option 3: View Statistics
```
1. Press: 7
2. See total items, claimed/unclaimed counts
3. View items breakdown by category
4. Press Enter to return to menu
```

### Option 4: Add a New Item
```
1. Press: 1
2. Generated ID will appear (e.g., ITEM006)
3. Enter item name: My Lost Keys
4. Enter category: Accessories
5. Enter location: Student Center
6. Item added successfully!
7. Press Enter to return to menu
```

### Option 5: Mark Item as Claimed
```
1. Press: 4
2. Enter item ID: ITEM001
3. Item marked as claimed
4. Press Enter to return to menu
```

### Option 6: Delete an Item
```
1. Press: 5
2. Enter item ID: ITEM002
3. Item deleted successfully
4. Press Enter to return to menu
```

### Option 7: Sort by Category
```
1. Press: 6
2. See all items grouped by category
3. Press Enter to return to menu
```

---

## 4. UNDERSTANDING THE APPLICATION

### Data Storage
- All items are stored in `items.json`
- This file is created automatically
- Changes are saved immediately

### Item Information Required
- **Item Name**: Name of the lost item
- **Category**: Type of item (Electronics, Clothing, etc.)
- **Location Found**: Where the item was found
- **Item ID**: Auto-generated unique identifier

### Item Status
- **Unclaimed**: Item waiting to be claimed
- **Claimed**: Item has been claimed

---

## 5. FILE DESCRIPTIONS

| File | Description |
|------|-------------|
| `lost_and_found.py` | Main application (run this file) |
| `items.json` | Data storage (auto-created/updated) |
| `README.md` | Detailed documentation |
| `test_demo.py` | Demo and test features |
| `requirements.txt` | Project dependencies (none required) |
| `QUICK_START.md` | This file |

---

## 6. SAMPLE DATA INCLUDED

The system comes with 5 sample items:

| ID | Item | Category | Location | Status |
|----|------|----------|----------|--------|
| ITEM001 | Blue Backpack | Accessories | Library Building | Unclaimed |
| ITEM002 | iPhone 14 | Electronics | Cafeteria | Claimed |
| ITEM003 | Gold Wedding Ring | Jewelry | Student Center | Unclaimed |
| ITEM004 | Red Hoodie | Clothing | Gymnasium | Unclaimed |
| ITEM005 | Student ID Card | Documents | Main Gate | Claimed |

---

## 7. TESTING THE SYSTEM

### Run Demo/Test File
```bash
python test_demo.py
```

This will show:
- Item class testing
- System operations
- Feature demonstrations
- Sample workflow
- JSON structure examples

---

## 8. KEYBOARD SHORTCUTS

| Action | Key |
|--------|-----|
| Confirm Input | Enter |
| Go Back to Menu | Press Enter after any operation |
| Cancel | Ctrl + C (exits application) |

---

## 9. TROUBLESHOOTING

### Problem: "Python not found"
**Solution**: Install Python or add it to PATH environment variables

### Problem: "ModuleNotFoundError"
**Solution**: Ensure you're in the correct directory and all files are in place

### Problem: "Permission denied" when saving
**Solution**: Check file permissions or move project to a writable location

### Problem: "JSON decode error"
**Solution**: Delete `items.json` and restart (will create new file automatically)

### Problem: How to start fresh?
**Solution**: Delete `items.json` file - new one will be created on next run

---

## 10. FEATURE CHECKLIST

- ✅ Add Lost Item
- ✅ View All Items
- ✅ Search Item (by name, category, location)
- ✅ Mark Item as Claimed
- ✅ Delete Item
- ✅ Sort Items by Category (Bonus)
- ✅ View Statistics (Bonus)
- ✅ JSON File Storage with Auto-Save
- ✅ Input Validation
- ✅ Error Handling

---

## 11. NEXT STEPS

After trying the basic operations:
1. Read `README.md` for detailed feature descriptions
2. Examine `lost_and_found.py` to understand the code structure
3. Try `test_demo.py` to see system capabilities
4. Customize categories to match your needs
5. Export/analyze the `items.json` file

---

## 12. TIPS FOR BEST RESULTS

1. **Use Descriptive Names**: Makes searching easier
2. **Consistent Categories**: Use similar category names
3. **Specific Locations**: Detailed location helps identification
4. **Regular Backups**: Copy `items.json` occasionally
5. **Keep it Running**: Items are saved to file, so no data loss

---

## 13. COMMON TASKS

### How to view all items?
Menu → Press 2 → View all items with statistics

### How to find a specific item?
Menu → Press 3 → Choose search type → Enter search term

### How to mark item as found/claimed?
Menu → Press 4 → Enter item ID → Item marked as claimed

### How to remove old items?
Menu → Press 5 → Enter item ID → Item deleted

### How to see unclaimed items count?
Menu → Press 7 → View statistics

---

## 14. CONTACT & SUPPORT

For issues or questions:
1. Check README.md for detailed documentation
2. Review test_demo.py for usage examples
3. Examine the code comments in lost_and_found.py

---

## 15. ENJOY!

You now have a fully functional Lost and Found Management System!
Happy organizing! 🎉

Start the application:
```bash
python lost_and_found.py
```

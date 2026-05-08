"""
Lost and Found Management System
A complete Python application for managing lost and found items using OOP and JSON storage.
"""

import json
import os
from datetime import datetime
from typing import List, Optional, Dict


class Item:
    """Represents a lost or found item."""
    
    def __init__(self, item_id: str, item_name: str, category: str, 
                 location_found: str, status: str = "Unclaimed"):
        """
        Initialize an Item object.
        
        Args:
            item_id: Unique identifier for the item
            item_name: Name of the item
            category: Category of the item
            location_found: Location where the item was found
            status: Status of the item (Unclaimed or Claimed)
        """
        self.item_id = item_id
        self.item_name = item_name
        self.category = category
        self.location_found = location_found
        self.status = status
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict:
        """Convert item to dictionary for JSON storage."""
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "category": self.category,
            "location_found": self.location_found,
            "status": self.status,
            "date_added": self.date_added
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Item':
        """Create an Item object from a dictionary."""
        item = Item(
            data["item_id"],
            data["item_name"],
            data["category"],
            data["location_found"],
            data.get("status", "Unclaimed")
        )
        item.date_added = data.get("date_added", item.date_added)
        return item
    
    def __str__(self) -> str:
        """String representation of the item."""
        return (f"ID: {self.item_id} | Name: {self.item_name} | "
                f"Category: {self.category} | Location: {self.location_found} | "
                f"Status: {self.status} | Date Added: {self.date_added}")


class LostAndFoundSystem:
    """Manages the lost and found items storage and operations."""
    
    def __init__(self, filename: str = "items.json"):
        """
        Initialize the Lost and Found Management System.
        
        Args:
            filename: Name of the JSON file to store items
        """
        self.filename = filename
        self.items: List[Item] = []
        self.load_items()
    
    def load_items(self) -> None:
        """Load items from JSON file. Handle missing file errors gracefully."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    data = json.load(file)
                    self.items = [Item.from_dict(item) for item in data]
                print(f"✓ Loaded {len(self.items)} items from {self.filename}")
            else:
                print(f"ℹ No existing file found. Starting with empty inventory.")
        except json.JSONDecodeError:
            print("⚠ Error: Corrupted JSON file. Starting with empty inventory.")
            self.items = []
        except Exception as e:
            print(f"⚠ Error loading items: {e}. Starting with empty inventory.")
            self.items = []
    
    def save_items(self) -> None:
        """Save all items to JSON file."""
        try:
            with open(self.filename, 'w') as file:
                data = [item.to_dict() for item in self.items]
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"✗ Error saving items: {e}")
    
    def generate_item_id(self) -> str:
        """Generate a unique item ID."""
        if not self.items:
            return "ITEM001"
        
        # Extract numbers from existing IDs and find the maximum
        max_id = 0
        for item in self.items:
            try:
                num = int(item.item_id.replace("ITEM", ""))
                max_id = max(max_id, num)
            except ValueError:
                continue
        
        return f"ITEM{max_id + 1:03d}"
    
    def validate_input(self, prompt: str, field_type: str = "str") -> str:
        """
        Validate user input.
        
        Args:
            prompt: The input prompt to display
            field_type: Type of validation (str, choice)
        
        Returns:
            Validated user input
        """
        while True:
            user_input = input(prompt).strip()
            
            if not user_input:
                print("✗ Input cannot be empty. Please try again.")
                continue
            
            if field_type == "str":
                if len(user_input) < 2:
                    print("✗ Input must be at least 2 characters long.")
                    continue
                return user_input
            
            return user_input
    
    def add_item(self) -> None:
        """Add a new lost item to the system."""
        print("\n" + "="*60)
        print("ADD LOST ITEM")
        print("="*60)
        
        item_id = self.generate_item_id()
        print(f"Generated Item ID: {item_id}")
        
        item_name = self.validate_input("Enter item name: ")
        
        print("\nCommon categories: Electronics, Clothing, Accessories, "
              "Jewelry, Documents, Other")
        category = self.validate_input("Enter category: ")
        
        location_found = self.validate_input("Enter location where item was found: ")
        
        new_item = Item(item_id, item_name, category, location_found)
        self.items.append(new_item)
        self.save_items()
        
        print(f"\n✓ Item added successfully!")
        print(f"  {new_item}")
    
    def view_all_items(self) -> None:
        """Display all items in a formatted table."""
        print("\n" + "="*60)
        print("ALL LOST AND FOUND ITEMS")
        print("="*60)
        
        if not self.items:
            print("ℹ No items in the system yet.")
            return
        
        print(f"\nTotal Items: {len(self.items)}\n")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        
        # Display statistics
        print("\n" + "-"*60)
        unclaimed = sum(1 for item in self.items if item.status == "Unclaimed")
        claimed = sum(1 for item in self.items if item.status == "Claimed")
        print(f"Unclaimed Items: {unclaimed} | Claimed Items: {claimed}")
    
    def search_item(self) -> None:
        """Search for items by name or category."""
        print("\n" + "="*60)
        print("SEARCH ITEM")
        print("="*60)
        
        if not self.items:
            print("ℹ No items in the system yet.")
            return
        
        print("\nSearch by:")
        print("1. Name")
        print("2. Category")
        print("3. Location Found")
        
        choice = self.validate_input("Enter your choice (1-3): ")
        
        if choice == "1":
            search_term = self.validate_input("Enter item name to search: ")
            results = [item for item in self.items 
                      if search_term.lower() in item.item_name.lower()]
        elif choice == "2":
            search_term = self.validate_input("Enter category to search: ")
            results = [item for item in self.items 
                      if search_term.lower() in item.category.lower()]
        elif choice == "3":
            search_term = self.validate_input("Enter location to search: ")
            results = [item for item in self.items 
                      if search_term.lower() in item.location_found.lower()]
        else:
            print("✗ Invalid choice. Please try again.")
            return
        
        if results:
            print(f"\n✓ Found {len(results)} item(s):\n")
            for i, item in enumerate(results, 1):
                print(f"{i}. {item}")
        else:
            print(f"✗ No items found matching '{search_term}'")
    
    def mark_as_claimed(self) -> None:
        """Mark an item as claimed by item ID."""
        print("\n" + "="*60)
        print("MARK ITEM AS CLAIMED")
        print("="*60)
        
        if not self.items:
            print("ℹ No items in the system yet.")
            return
        
        item_id = self.validate_input("Enter item ID to mark as claimed: ")
        
        for item in self.items:
            if item.item_id.lower() == item_id.lower():
                if item.status == "Claimed":
                    print(f"ℹ Item {item_id} is already marked as claimed.")
                else:
                    item.status = "Claimed"
                    self.save_items()
                    print(f"✓ Item {item_id} has been marked as claimed!")
                    print(f"  {item}")
                return
        
        print(f"✗ Item with ID '{item_id}' not found.")
    
    def delete_item(self) -> None:
        """Delete an item from the system using item ID."""
        print("\n" + "="*60)
        print("DELETE ITEM")
        print("="*60)
        
        if not self.items:
            print("ℹ No items in the system yet.")
            return
        
        item_id = self.validate_input("Enter item ID to delete: ")
        
        for i, item in enumerate(self.items):
            if item.item_id.lower() == item_id.lower():
                removed_item = self.items.pop(i)
                self.save_items()
                print(f"✓ Item {item_id} has been deleted successfully!")
                print(f"  Deleted: {removed_item}")
                return
        
        print(f"✗ Item with ID '{item_id}' not found.")
    
    def sort_by_category(self) -> None:
        """Sort and display items by category."""
        print("\n" + "="*60)
        print("ITEMS SORTED BY CATEGORY")
        print("="*60)
        
        if not self.items:
            print("ℹ No items in the system yet.")
            return
        
        # Group items by category
        categories = {}
        for item in self.items:
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)
        
        # Display items grouped by category
        for category in sorted(categories.keys()):
            print(f"\n{category.upper()} ({len(categories[category])} items):")
            print("-" * 60)
            for i, item in enumerate(categories[category], 1):
                print(f"{i}. {item}")
    
    def count_statistics(self) -> None:
        """Display item statistics."""
        print("\n" + "="*60)
        print("ITEM STATISTICS")
        print("="*60)
        
        if not self.items:
            print("ℹ No items in the system yet.")
            return
        
        total = len(self.items)
        unclaimed = sum(1 for item in self.items if item.status == "Unclaimed")
        claimed = sum(1 for item in self.items if item.status == "Claimed")
        
        print(f"\nTotal Items: {total}")
        print(f"Unclaimed Items: {unclaimed} ({unclaimed/total*100:.1f}%)")
        print(f"Claimed Items: {claimed} ({claimed/total*100:.1f}%)")
        
        # Category breakdown
        categories = {}
        for item in self.items:
            categories[item.category] = categories.get(item.category, 0) + 1
        
        print(f"\nItems by Category:")
        for category in sorted(categories.keys()):
            print(f"  {category}: {categories[category]}")


class LostAndFoundApp:
    """Main application class to manage the menu and user interactions."""
    
    def __init__(self):
        """Initialize the application."""
        self.system = LostAndFoundSystem()
    
    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "="*60)
        print("LOST AND FOUND MANAGEMENT SYSTEM")
        print("="*60)
        print("\n1. Add Lost Item")
        print("2. View All Items")
        print("3. Search Item")
        print("4. Mark Item as Claimed")
        print("5. Delete Item")
        print("6. Sort Items by Category (BONUS)")
        print("7. View Statistics (BONUS)")
        print("8. Exit")
        print("-"*60)
    
    def run(self) -> None:
        """Run the application main loop."""
        print("\n" + "*"*60)
        print("Welcome to Lost and Found Management System")
        print("*"*60)
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == "1":
                self.system.add_item()
            elif choice == "2":
                self.system.view_all_items()
            elif choice == "3":
                self.system.search_item()
            elif choice == "4":
                self.system.mark_as_claimed()
            elif choice == "5":
                self.system.delete_item()
            elif choice == "6":
                self.system.sort_by_category()
            elif choice == "7":
                self.system.count_statistics()
            elif choice == "8":
                print("\n✓ Thank you for using Lost and Found Management System!")
                print("  All changes have been saved.")
                break
            else:
                print("\n✗ Invalid choice. Please enter a number between 1 and 8.")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = LostAndFoundApp()
    app.run()

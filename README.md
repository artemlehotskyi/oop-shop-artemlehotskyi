# 🐍 Python OOP — Shop & User Management

> Object-Oriented Programming tasks implemented in Python.  
> Covers class inheritance, encapsulation, polymorphism and modular code structure.

---

## 📦 Task 1 — Online Shop

### What was done:
- Created a base class `Shop` with attributes `shop_name`, `store_type`, `number_of_units`
- Implemented methods `describe_shop()`, `open_shop()`, `set_number_of_units()`, `increment_number_of_units()`
- Created multiple instances of `Shop`
- Built a subclass `Discount` that inherits from `Shop` with a `discount_products` list and `get_discount_products()` method
- Moved the `Shop` class to a separate module `shop.py` and imported it in `main_shop.py`

### Files:
| File | Description |
|------|-------------|
| `shop.py` | `Shop` and `Discount` classes |
| `main_shop.py` | Imports `Shop`, creates `all_store` instance |

---

## 👤 Task 2 — User Account Management

### What was done:
- Created a class `User` with attributes `first_name`, `last_name`, `email`, `age`, `password`, `phone_number`, `login_attempts`
- Implemented methods `describe_user()`, `greetings_user()`, `increment_login_attempts()`, `reset_login_attempts()`
- Created multiple user instances and called all methods
- Built a subclass `Admin` that inherits from `User` with a `Privileges` object as an attribute
- Created a separate class `Privileges` with a `privileges` list and `show_privileges()` method
- Split classes into modules: `user.py` and `admin.py`, tested imports in `main_user.py`

### Files:
| File | Description |
|------|-------------|
| `user.py` | `User` class |
| `admin.py` | `Privileges` and `Admin` classes |
| `main_user.py` | Imports `Admin`, calls `show_privileges()` |

---

## 🚀 Concepts Covered

- ✅ Classes & instances
- ✅ `__init__` method & attributes
- ✅ Instance methods
- ✅ Default attribute values
- ✅ Inheritance & `super()`
- ✅ Composition (class as attribute of another class)
- ✅ Modular code with `import`

---

## ▶️ How to Run

```bash
# Run Shop task
python main_shop.py

# Run User task
python main_user.py
```

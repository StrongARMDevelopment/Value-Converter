# Imperial to Decimal Converter

This is a simple GUI application built with Python and Tkinter that converts imperial measurements (feet and inches) into decimal feet.

## 🔧 Features

* Accepts a wide range of input formats:

  * `1' 6"`
  * `1' 6-1/2"`
  * `6 1/2"`
  * `1'`
  * `6"`
  * `1/2"`
  * `6in`
* Converts input to decimal feet rounded to three decimal places.
* Copies the result to clipboard with one click.
* Shows error messages for invalid input.
* Logs and displays all errors in a dedicated error log window.

## 🖥️ How to Use

1. Run the script.
2. Enter a measurement in the input field (e.g., `2' 3-1/4"`).
3. Press `Enter` or click **Convert**.
4. The decimal result will appear below.
5. Click **Copy** to copy the output.
6. Click **View Error Log** to review any issues.

## 📦 Dependencies

* Python 3.x
* Tkinter (standard with Python)
* `re` module (standard library)

## 🧪 Example

**Input:** `1' 6-1/2"`
**Output:** `1.542`

---

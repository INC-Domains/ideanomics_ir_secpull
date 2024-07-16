function clearSheet(){
  const sheetName = 'Sheet1'; // Replace with your sheet name
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
  const lastRow = sheet.getLastRow();
    if (lastRow > 1) {
      const range = sheet.getRange(2, 1, lastRow - 1, sheet.getLastColumn());
      range.clearContent(); // Clears all the content in the range
    }
}
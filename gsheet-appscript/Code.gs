function doPost(e) {
  try {
    const sheetName = 'Sheet1'; // Replace with your sheet name
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(sheetName);
    if (!sheet) {
      throw new Error('Sheet not found');
    }

    // Parse the data from the POST request
    const jsonData = JSON.parse(e.postData.contents);

    // Prepare an array to hold all rows to be appended
    const rows = jsonData.map(data => [
      data["Form & File"],
      data["File date"],
      data["Reporting for date"],
      data["Filing Type"],
      data["File link"]
    ]);

    // Append all rows to the sheet
    sheet.getRange(sheet.getLastRow() + 1, 1, rows.length, rows[0].length).setValues(rows);

    return ContentService.createTextOutput(JSON.stringify({ status: 'success', message: 'Data inserted successfully' }))
                         .setMimeType(ContentService.MimeType.JSON);
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: 'error', message: error.message }))
                         .setMimeType(ContentService.MimeType.JSON);
  }
}

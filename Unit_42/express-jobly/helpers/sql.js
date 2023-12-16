const { BadRequestError } = require("../expressError");

/** Helper for making selective update queries.
 * Calling function can use to make the SET clause of an UPDATE to SQL stmt.

@param dataToUpdate is an object {field1: newVal, field2: newVal, etc.}
@param jsToSql is an object; it maps js-style data fields to database column names like {firstName: 'first_name', age: 'age' }

@returns and object {sqlSetCols, dataToUpdate}

@example {firstName: 'Aliya', age: 32 } => {setCols: 32'"first_name"=$1, "age"=$2', values: ['Aliya', 6]}

*/

function sqlForPartialUpdate(dataToUpdate, jsToSql) {
  const keys = Object.keys(dataToUpdate);
  if (keys.length === 0) throw new BadRequestError("No data");

  // {firstName: 'Aliya', age: 32} => ['"first_name"=$1', '"age"=$2']
  const cols = keys.map((colName, idx) =>
      `"${jsToSql[colName] || colName}"=$${idx + 1}`,
  );

  return {
    setCols: cols.join(", "),
    values: Object.values(dataToUpdate),
  };
}

module.exports = { sqlForPartialUpdate };

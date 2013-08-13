<h2>{{Age}}</h2>
<form method="GET" action="/">
  <fieldset>
  <label>Age: <input name="guess" type="text"></label>
  <input type="radio" name="age" value="G">G<br>
  <input type="radio" name="age" value="Teen">Teen<br>
  <input type="radio" name="age" value="Mature">Mature<br>
  <label>Type:</label><br>
  <select name="type">
     <option> Movies </option>
     <option> Series </option>
  </select>
  <br>
  <label>Genres:</label><br>
  <input type="checkbox" name="action" value="1"> Action
  <input type="checkbox" name="action" value="1"> Adventure
  <input type="checkbox" name="action" value="1"> Comedy
  <input type="checkbox" name="action" value="1"> Romance
  <input type="checkbox" name="action" value="1"> Sports
  <input type="checkbox" name="action" value="1"> Ecchi
  <input type="checkbox" name="action" value="1"> Science Fiction
  </fieldset>
  <button type="submit">Submit my form</button>
</form>




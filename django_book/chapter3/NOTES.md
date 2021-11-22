**Rendering a page dynamically:**  
1. `HTTPRequest` by the browser with locator `time/`
2. Controller URLConf maps `time/` to view generator function `current_datetime`
3. Data is injected by `datetime.now` (a.k.a the Model) into the view
3. View: function view returns an `HTTPResponse`
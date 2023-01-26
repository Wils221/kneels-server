import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_single_metal, create_metal, update_metal
from views import get_all_styles, get_single_style, create_style
from views import get_all_sizes, get_single_size, create_size
from views import get_all_orders, get_single_order, create_order, delete_order, update_order


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def parse_url(self, path):
        """_summary_

        Args:
            path (_type_): _description_

        Returns:
            _type_: _description_
        """
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a class function
    def do_GET(self):
        """Handles GET requests to the server """
        response = {} #Default response

        #Parse the URL and capture the tuple that is returned
        (resource, id) = self.parse_url(self.path)

        #Check the path, return the correlating response
        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)

                if response is not None:
                    self._set_headers(200)

                elif response is None:
                    self._set_headers(404)
                    response = { "message": "That metal is not currently in stock for jewelry." }

            else:
                self._set_headers(200)
                response = get_all_metals()
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)

                if response is not None:
                    self._set_headers(200)

                elif response is None:
                    self._set_headers(404)
                    response = { "message": "That size is not currently in stock for jewelry." }

            else:
                self._set_headers(200)
                response = get_all_sizes()
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)

                if response is not None:
                    self._set_headers(200)

                elif response is None:
                    self._set_headers(404)
                    response = { "message": "That style is not currently in stock for jewelry." }

            else:
                self._set_headers(200)
                response = get_all_styles()
        elif resource == "pieces":
            if id is not None:
                response = get_single_style(id)

                if response is not None:
                    self._set_headers(200)

                elif response is None:
                    self._set_headers(404)
                    response = { "message": "That piece is not currently in stock for jewelry." }

            else:
                self._set_headers(200)
                response = get_all_styles()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)

                if response is not None:
                    self._set_headers(200)

                elif response is None:
                    self._set_headers(404)
                    response = { "message": "That order was never placed, or was cancelled." }

            else:
                self._set_headers(200)
                response = get_all_orders()

        #Send a JSON formatted string as a response
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server"""

        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        if resource == "orders":
            new_order = None
            new_order = create_order(post_body)
            self.wfile.write(json.dumps(new_order).encode())

    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single order from the list
        if resource == "orders":
            delete_order(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        success = False

        if resource == "metals":
            success = update_metal(id, post_body)

            if success:
                self._set_headers(204)
            else:
                self._set_headers(404)

            # Encode the new resource and send in response
            self.wfile.write("".encode())

        # Update a single resource from the list
        elif resource == "orders":
            self._set_headers(403)
            update_order(id, post_body)
            response = {"message": "Order has been accepted. Modification requires contacting the company directly."}
            self.wfile.write(json.dumps(response).encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()



# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
			---MY SQL PROJECT---
			
	I decided to make my database use anime shows
	as its content. Although I took some liberties
	forcing some relationships, I was able to show
	all three of the database relationships.
	Realistically there isn't many things that have
	a one-to-one or a one-to-many relationship so
	I thought it was a fine choice.
	
	
			---Reference Table---
			
	| Name      | Table | Method | Parameters | Description                              |
	| ---------------------------------------------------------------------------------- |
	| index     | anime | GET    | none       | Selects all items from the table         |
	| show      | anime | GET    | id         | Selects a specific record from the table |
	| create    | anime | POST   | none       | Creates a new record on the table        |
	| delete    | anime | DELETE | id         | Deletes a specific record from the table |
	| get_genres| anime | GET    | id         | Gets the genres for a specific record    |
	
	
			---Questions---
			
	1. How did the project's design evolve over time?
		This project didn't really change from the original design.
		
	2. Did you choose to use an ORM or raw SQL? Why?
		I chose ORM because I thought raw SQL would be too simple while ORM required some learning.
        
	3. What future improvements are in store, if any?
		I still need to create endpoints for the rest of my tables as well as add data to them.
	
	
	
	
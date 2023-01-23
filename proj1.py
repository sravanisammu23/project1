// Loop through each user
foreach (User u in users) { 
  // Get the user preferences 
  List<String> preferences = u.getPreferences(); 

  // Loop through each available seat
  foreach (Seat s in seats) { 
    // Check if seat meets user preferences 
    if (s.meetsRequirements(preferences)) { 
      // Allocate the seat to the user 
      u.allocateSeat(s); 
      break; 
      } 
    } 
}
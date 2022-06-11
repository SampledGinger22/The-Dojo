List<Eruption> eruptions = new List<Eruption>()
{
    new Eruption("La Palma", 2021, "Canary Is", 2426, "Stratovolcano"),
    new Eruption("Villarrica", 1963, "Chile", 2847, "Stratovolcano"),
    new Eruption("Chaiten", 2008, "Chile", 1122, "Caldera"),
    new Eruption("Kilauea", 2018, "Hawaiian Is", 1122, "Shield Volcano"),
    new Eruption("Hekla", 1206, "Iceland", 1490, "Stratovolcano"),
    new Eruption("Taupo", 1910, "New Zealand", 760, "Caldera"),
    new Eruption("Lengai, Ol Doinyo", 1927, "Tanzania", 2962, "Stratovolcano"),
    new Eruption("Santorini", 46,"Greece", 367, "Shield Volcano"),
    new Eruption("Katla", 950, "Iceland", 1490, "Subglacial Volcano"),
    new Eruption("Aira", 766, "Japan", 1117, "Stratovolcano"),
    new Eruption("Ceboruco", 930, "Mexico", 2280, "Stratovolcano"),
    new Eruption("Etna", 1329, "Italy", 3320, "Stratovolcano"),
    new Eruption("Bardarbunga", 1477, "Iceland", 2000, "Stratovolcano")
};
// Example Query - Prints all Stratovolcano eruptions
// IEnumerable<Eruption> stratovolcanoEruptions = eruptions.Where(c => c.Type == "Stratovolcano");
// PrintEach(stratovolcanoEruptions, "Stratovolcano eruptions.");
    // Item 1
// IEnumerable<Eruption> stratovolcanoEruptions = eruptions.Where(c => c.Location == "Chile");
// PrintEach(stratovolcanoEruptions, "Stratovolcano eruptions.");
    // Item 2
// List<Eruption> HawaiianEruptions = eruptions
//                                 .Where(c => c.Location == "Hawaiian Is")
//                                 .OrderBy(x =>x.Year).ToList();
// if(HawaiianEruptions[0] == null)
// {
//     Console.WriteLine("No Hawaiian Is. Eruption Found");
// }
// else
// {
// Console.WriteLine(HawaiianEruptions[0].ToString());
// }
    // Item 3
// List<Eruption> NewZealandErupt = eruptions
//                                 .Where(c => c.Location == "New Zealand" && c.Year > 1900)
//                                 .OrderBy(x =>x.Year).ToList();
// Console.WriteLine(NewZealandErupt[0].ToString());
    //Item 4
// IEnumerable<Eruption> Elevation2000 = eruptions.Where(c => c.ElevationInMeters > 2000);
// PrintEach(Elevation2000, "These are all over 2000m");
    //Item 5
// IEnumerable<Eruption> zname = eruptions.Where(c => c.Volcano.StartsWith("Z"));
// PrintEach(zname, "The number of items in this list is: " + zname.Count().ToString());
    //Item 6
// List<Eruption> maxelevation = eruptions.OrderBy(x => x.ElevationInMeters == int.MaxValue).ToList();
// Console.WriteLine("The max elevation in this list is: " + maxelevation[0].ElevationInMeters + " Meters");
    //Item 7
// List<Eruption> maxelevation = eruptions.OrderBy(x => x.ElevationInMeters == int.MaxValue).ToList();
// Console.WriteLine("The volcano with the highest elevation is: " + maxelevation[0].Volcano);
    //Item 8
// IEnumerable<Eruption> alphabetical = eruptions.OrderBy(c => c.Volcano);
// PrintEach(alphabetical, "Here are all volcanoes in alphabetical order");
    //Item 9
IEnumerable<Eruption> alphabeticalwyear = eruptions
                            .OrderBy(c => c.Volcano)
                            .Where(x => x.Year > 1000);
PrintEach(alphabeticalwyear, "Here are all eruptions newer than 1000 CE in alphabetical order");
// to make the volcano names only print, edit line 70 to item.Volcano.ToString()


// Execute Assignment Tasks here!
 
// Helper method to print each item in a List or IEnumerable.This should remain at the bottom of your class!
static void PrintEach(IEnumerable<dynamic> items, string msg = "")
{
    Console.WriteLine("\n" + msg);
    foreach (var item in items)
    {
        Console.WriteLine(item.ToString());
    }
}

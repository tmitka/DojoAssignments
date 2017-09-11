using System;
using System.Collections.Generic;
using System.Linq;
using JsonData;

namespace ConsoleApplication
{
    public class Program
    {
        public static void Main(string[] args)
        {
            //Collections to work with
            List<Artist> Artists = JsonToFile<Artist>.ReadJson();
            List<Group> Groups = JsonToFile<Group>.ReadJson();

            //========================================================
            //Solve all of the prompts below using various LINQ queries
            //========================================================

            //There is only one artist in this collection from Mount Vernon, what is their name and age?
            Artist FromMtVernon = Artists.Where(artist => artist.Hometown == "Mount Vernon").Single();
            Console.WriteLine($"The artist {FromMtVernon.ArtistName} from Mt Vernon is {FromMtVernon.Age} years old");
            //Who is the youngest artist in our collection of artists?
            Artist Youngest = Artists.OrderBy(artist => artist.Age).First();
            Console.WriteLine($"The Youngest artist is {Youngest.ArtistName}");
            //Display all artists with 'William' somewhere in their real name
            List<Artist> Williams = Artists.Where(artist => artist.RealName.Contains("William")).ToList();
            Console.WriteLine("The Following artists have William in their real names:");
            foreach(var artist in Williams) {
                Console.WriteLine(artist.ArtistName + " - " + artist.RealName);
            }

            //Display the names of all groups less than 8 characters in length
            List<Group> groupByLength = Groups.Where(group => group.GroupName.Length < 8).ToList();
            Console.WriteLine("All groups with names less than 8 in length:");
            foreach(var group in groupByLength){
                Console.WriteLine(group.GroupName);
            }

            //Display the 3 oldest artist from Atlanta
            List<Artist> Oldest = Artists.Where(artist=> artist.Hometown == "Atlanta")
                                    .OrderByDescending(artist => artist.Age)
                                    .Take(3)
                                    .ToList();
            Console.WriteLine("The three oldest artists from Atlanta are:");
            foreach(var artist in Oldest) {
                Console.WriteLine(artist.ArtistName + " - " + artist.Age);
            }
            //(Optional) Display the Group Name of all groups that have members that are not from New York City
            List<string> NonNewYorkGroups = Artists
                                .Join(Groups, artist => artist.GroupId, group => group.Id, (artist, group) => { artist.Group = group; return artist;})
                                .Where(artist => (artist.Hometown != "New York City" && artist.Group != null))
                                .Select(artist => artist.Group.GroupName)
                                .Distinct()
                                .ToList();
            Console.WriteLine("All groups with members not from New York City:");
            foreach(var group in NonNewYorkGroups){
                Console.WriteLine(group);
            }

            //(Optional) Display the artist names of all members of the group 'Wu-Tang Clan'
            Group WuTang = Groups.Where(group => group.GroupName == "Wu-Tang Clan")
                                    .GroupJoin(Artists, 
                                        group => group.Id,
                                        artist => artist.GroupId,
                                        (group, artists) => { group.Members = artists.ToList(); return group;})
                                    .Single();
            Console.WriteLine("List of Artist in the Wu-Tang Clan:");
            foreach(var artist in WuTang.Members){
                Console.WriteLine(artist.ArtistName);
            }
        }
    }
}
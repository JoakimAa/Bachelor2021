using Bachelor2021.DataAccess;
using Bachelor2021.Model;
using Microsoft.Data.SqlClient;
using Microsoft.EntityFrameworkCore;
using System;

namespace Bachelor2021.DataAcess.Maintenance {
    class Program {
        static void Main(string[] args) {
            var connection = @"Server=(localdb)\MSSQLLocalDB;Database=Bachelor2021;Trusted_Connection=True;ConnectRetryCount=0";

            var optionsBuilder = new DbContextOptionsBuilder<DataContext>();
            optionsBuilder.UseSqlServer(connection, x => x.MigrationsAssembly("Bachelor2021.DataAccess.Maintenance"));

            //PopulateDatabase(optionsBuilder);
            //QueryData(optionsBuilder);
        }

        private static void QueryData(DbContextOptionsBuilder<DataContext> optionsBuilder) {
            using (var db = new DataContext(optionsBuilder.Options)) {
                var receipts = db.Receipts;
                Console.WriteLine("Bachelor2021: \n");
                foreach (var receipt in receipts) {
                    Console.WriteLine("Id: {0}", receipt.ReceiptId);
                    Console.WriteLine("Amount: {0}", receipt.Amount);
                    Console.WriteLine("Type: {0}", receipt.Type);
                    Console.WriteLine("Company: {0}", receipt.Company);
                    Console.WriteLine("Date: {0}", receipt.Date);
                    Console.WriteLine("\n");
                }
            }
        }

        private static void PopulateDatabase(DbContextOptionsBuilder<DataContext> optionsBuilder) {
            try {
                using (var data = new DataContext(optionsBuilder.Options)) {

                    // Create receipts
                    var receipt = new Receipt() { Amount = 200, Type = "Kvittering", Company = "Vy", Date = "23.02.2021 22:00"};
                    var receipt2 = new Receipt() { Amount = 300, Type = "Faktura", Company = "Vy", Date = "23.02.2021 23:00"};

                    data.Add(receipt);
                    data.Add(receipt2);
                    data.SaveChanges();
                }
            }
            catch (SqlException sqlex) {
                Console.WriteLine(sqlex.Message);
            }
        }
    }
}

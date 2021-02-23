using Bachelor2021.DataAccess;
using Bachelor2021.Model;
using Microsoft.Data.SqlClient;
using Microsoft.EntityFrameworkCore;
using System;

namespace Bachelor2021.DataAcess.Maintenance {
    class Program {
        static void Main(string[] args) {
            var connection = @"Server=(localdb)\MSSQLLocalDB;Database=Bachelor2021;Trusted_Connection=True;ConnectRetryCount=0";

            var optionsBuilder = new DbContextOptionsBuilder<ReceiptContext>();
            optionsBuilder.UseSqlServer(connection, x => x.MigrationsAssembly("Bachelor2021.DataAccess.Maintenance"));

            //PopulateDatabase(optionsBuilder);
            //QueryData(optionsBuilder);
        }

        private static void QueryData(DbContextOptionsBuilder<ReceiptContext> optionsBuilder) {
            using (var db = new ReceiptContext(optionsBuilder.Options)) {
                var receipts = db.Receipts;
                Console.WriteLine("Bachelor2021: \n");
                foreach (var receipt in receipts) {
                    Console.WriteLine("{0}:", receipt.ReceiptId);
                    Console.WriteLine("{0}:", receipt.Amount);
                    Console.WriteLine("{0}:", receipt.Type);
                    Console.WriteLine("{0}:", receipt.Company);
                    Console.WriteLine("{0}:", receipt.Date);
                }
            }
        }

        private static void PopulateDatabase(DbContextOptionsBuilder<ReceiptContext> optionsBuilder) {
            try {
                using (var data = new ReceiptContext(optionsBuilder.Options)) {

                    // Create receipts
                    var receipt = new Receipt() { Amount = 200, Type = "Kvittering", Company = "Vy", Date = "23.02.2021"};
                    var receipt2 = new Receipt() { Amount = 300, Type = "Faktura", Company = "Vy", Date = "23.02.2021"};

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

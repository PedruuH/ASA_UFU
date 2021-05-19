import express from "express";
import * as dotenv from "dotenv";
import * as apiRoutes from "./routes/allRoutes";

dotenv.config();

// rest of the code remains same
const app = express();
const PORT = process.env.PORT || 5000;
app.use(express.json());
app.use("/", apiRoutes.allRoutes);

app.listen(PORT, () => {
  console.log(`⚡️[server]: Ta rodando https://localhost:${PORT}`);
});

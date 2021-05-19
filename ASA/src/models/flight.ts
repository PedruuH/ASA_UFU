import { Airport } from "./airport";

export interface Flight {
  code: string;
  start: Airport;
  end: Airport;
  capacity: number;
  departureTime: number;
  arrivalTime: number;
  tax: number;
  price: number;
}

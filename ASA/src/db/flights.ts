import { Flight } from "../models/flight";
import { getAllAirports } from "./airports";
import { parseISO, isSameDay } from "date-fns";

const airports = getAllAirports();
const flights: Flight[] = [
  {
    code: "VOO-001",
    start: airports[0],
    end: airports[1],
    departureTime: Date.parse("2021-05-01 22:00"),
    capacity: 50,
    arrivalTime: Date.parse("2021-05-01 00:00"),
    tax: 59.3,
    price: 230.0,
  },
  {
    code: "VOO-002",
    start: airports[1],
    end: airports[2],
    capacity: 50,
    departureTime: Date.parse("2021-06-01 22:00"),
    arrivalTime: Date.parse("2021-06-02 00:00"),
    tax: 50.3,
    price: 220.0,
  },
  {
    code: "VOO-003",
    start: airports[0],
    end: airports[2],
    capacity: 50,
    departureTime: Date.parse("2021-06-01 21:00"),
    arrivalTime: Date.parse("2021-06-02 00:00"),
    tax: 30.3,
    price: 220.0,
  },
  {
    code: "VOO-004",
    start: airports[0],
    end: airports[2],
    capacity: 50,
    departureTime: Date.parse("2021-06-01 21:00"),
    arrivalTime: Date.parse("2021-06-02 00:00"),
    tax: 0.3,
    price: 220.0,
  },
];
// 6 - RETORNAR VOOS
export function findByDate(date: string): Flight[] | null {
  const refDate = parseISO(date);

  const retorno = flights.filter((flight) => {
    if (isSameDay(flight.departureTime, refDate)) return flight;
  });
  return retorno;
}

export function findAll(): Flight[] {
  return flights;
}

export function findByCode(code: string): Flight | null {
  const retorno = flights.filter((flight) => {
    if (flight.code === code) return flight;
  });
  return retorno[0] ?? null;
}

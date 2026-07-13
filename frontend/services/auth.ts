import { api } from "@/services/api";
import type { TokenResponse } from "@/types/auth";
import type { User } from "@/types/user";

export async function login(
  email: string,
  password: string,
): Promise<TokenResponse> {
  const formData = new URLSearchParams();

  formData.append("username", email);
  formData.append("password", password);

  console.log("1. Before Request");

  const { data } = await api.post<TokenResponse>("/auth/login", formData, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });

  console.log("2. Response:", data);

  return data;
}

export async function getCurrentUser(): Promise<User> {
  const { data } = await api.get<User>("/auth/me");

  return data;
}

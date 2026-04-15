import { Tabs } from "expo-router";

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: "#4f46e5",
        tabBarInactiveTintColor: "#a1a1aa",
        tabBarStyle: { borderTopColor: "#f4f4f5" },
        headerShown: false,
      }}
    >
      <Tabs.Screen name="index" options={{ title: "Journal", tabBarIcon: ({ color }) => <TabIcon emoji="📓" color={color} /> }} />
      <Tabs.Screen name="checkin" options={{ title: "Check in", tabBarIcon: ({ color }) => <TabIcon emoji="✏️" color={color} /> }} />
      <Tabs.Screen name="insights" options={{ title: "Insights", tabBarIcon: ({ color }) => <TabIcon emoji="🔍" color={color} /> }} />
      <Tabs.Screen name="profile" options={{ title: "Profile", tabBarIcon: ({ color }) => <TabIcon emoji="👤" color={color} /> }} />
    </Tabs>
  );
}

function TabIcon({ emoji, color }: { emoji: string; color: string }) {
  const { Text } = require("react-native");
  return <Text style={{ fontSize: 20, opacity: color === "#4f46e5" ? 1 : 0.5 }}>{emoji}</Text>;
}
